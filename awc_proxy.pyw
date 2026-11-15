from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from logging.handlers import RotatingFileHandler
from urllib.parse import parse_qs, urlencode, urlparse
import logging
import os
import re
import threading
import time
import urllib.request

HOST = "127.0.0.1"
PORT = 8765
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FALLBACK_DIR = r"C:\Users\PC\Documents\WeatherWallpaper"
BASE_DIR = SCRIPT_DIR if os.path.isfile(os.path.join(SCRIPT_DIR, "controls.html")) else FALLBACK_DIR
LOG_PATH = os.path.join(SCRIPT_DIR, "awc_proxy.log")

CACHE_TTL_SECONDS = 300
MAX_STALE_SECONDS = 5400

ALLOWED_STATIC_FILES = {
    "/": ("controls.html", "text/html; charset=utf-8"),
    "/controls.html": ("controls.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/wallpaper.js": ("wallpaper.js", "application/javascript; charset=utf-8"),
    "/wallpaper.jpg": ("wallpaper.jpg", "image/jpeg"),
    "/masks/custom_masks_packed.png": (os.path.join("masks", "custom_masks_packed.png"), "image/png"),
}

logger = logging.getLogger("awc_proxy")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(LOG_PATH, maxBytes=262144, backupCount=1, encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(handler)

cache_lock = threading.Lock()
fetch_locks_guard = threading.Lock()
fetch_locks = {}
metar_cache = {}

static_cache_lock = threading.Lock()
static_cache = {}


class ExclusiveThreadingHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = False
    daemon_threads = True


class AwcProxyHandler(BaseHTTPRequestHandler):
    def _send_common_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Accept, Content-Type")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Cache-Control", "no-store")

    def _serve_static_file(self, filename, content_type):
        file_path = os.path.join(BASE_DIR, filename)
        if not os.path.isfile(file_path):
            logger.warning("Static file not found: %s (BASE_DIR=%s)", filename, BASE_DIR)
            self.send_response(404)
            self._send_common_headers()
            self.end_headers()
            return

        try:
            mtime = os.path.getmtime(file_path)
            data = None
            with static_cache_lock:
                entry = static_cache.get(file_path)
                if entry and entry["mtime"] == mtime:
                    data = entry["data"]

            if data is None:
                with open(file_path, "rb") as f:
                    data = f.read()
                with static_cache_lock:
                    static_cache[file_path] = {"mtime": mtime, "data": data}

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Accept, Content-Type")
            self.send_header("Access-Control-Allow-Private-Network", "true")
            self.send_header("Cache-Control", "public, max-age=60")
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            logger.debug("STATIC 200 %s (%d bytes)", filename, len(data))
        except Exception as err:
            logger.error("Failed to serve static file %s: %s", filename, err)
            self.send_response(500)
            self._send_common_headers()
            self.end_headers()

    def _send_json_bytes(self, status_code, body):
        self.send_response(status_code)
        self._send_common_headers()
        if body:
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._send_common_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path in ALLOWED_STATIC_FILES:
            filename, content_type = ALLOWED_STATIC_FILES[parsed.path]
            self._serve_static_file(filename, content_type)
            return

        if parsed.path != "/metar":
            logger.warning("404 Not Found: %s", parsed.path)
            self.send_response(404)
            self._send_common_headers()
            self.end_headers()
            return

        params = parse_qs(parsed.query)
        icao = params.get("ids", ["VVNB"])[0].strip().upper()
        hours = params.get("hours", ["2"])[0].strip()

        if not re.fullmatch(r"[A-Z0-9]{4}", icao) or not hours.isdigit() or not (1 <= int(hours) <= 24):
            logger.warning("Bad request params: ids=%s hours=%s", icao, hours)
            self.send_response(400)
            self._send_common_headers()
            self.end_headers()
            return

        cache_key = (icao, hours)
        now = time.time()

        with cache_lock:
            cached_entry = metar_cache.get(cache_key)
            if cached_entry and (now - cached_entry["fetched_at"]) < CACHE_TTL_SECONDS:
                age_sec = int(now - cached_entry["fetched_at"])
                logger.info("METAR CACHE_HIT %s (age=%ds)", icao, age_sec)
                self._send_json_bytes(200, cached_entry["body"])
                return

        with fetch_locks_guard:
            if cache_key not in fetch_locks:
                fetch_locks[cache_key] = threading.Lock()
            f_lock = fetch_locks[cache_key]

        with f_lock:
            now = time.time()
            with cache_lock:
                cached_entry = metar_cache.get(cache_key)
                if cached_entry and (now - cached_entry["fetched_at"]) < CACHE_TTL_SECONDS:
                    age_sec = int(now - cached_entry["fetched_at"])
                    logger.info("METAR CACHE_HIT %s (age=%ds, synchronized)", icao, age_sec)
                    self._send_json_bytes(200, cached_entry["body"])
                    return

            target_url = "https://aviationweather.gov/api/data/metar?" + urlencode(
                {"ids": icao, "format": "json", "hours": hours}
            )

            start_ms = time.perf_counter()
            try:
                req = urllib.request.Request(
                    target_url,
                    headers={
                        "User-Agent": "WeatherWallpaperLocalProxy/1.0",
                        "Accept": "application/json",
                    },
                )
                with urllib.request.urlopen(req, timeout=10) as resp:
                    body = resp.read()
                    elapsed_ms = int((time.perf_counter() - start_ms) * 1000)
                    if resp.status == 200 and body:
                        with cache_lock:
                            metar_cache[cache_key] = {"fetched_at": time.time(), "body": body}
                    logger.info("METAR UPSTREAM_%s %s (%dms, %d bytes)", resp.status, icao, elapsed_ms, len(body))
                    self._send_json_bytes(resp.status, body)
            except Exception as err:
                elapsed_ms = int((time.perf_counter() - start_ms) * 1000)
                logger.warning("METAR UPSTREAM_ERR %s (%dms): %s", icao, elapsed_ms, err)
                with cache_lock:
                    stale_entry = metar_cache.get(cache_key)
                if stale_entry and (time.time() - stale_entry["fetched_at"]) < MAX_STALE_SECONDS:
                    logger.info("METAR STALE_SERVED %s", icao)
                    self._send_json_bytes(200, stale_entry["body"])
                    return
                self.send_response(502)
                self._send_common_headers()
                self.end_headers()

    def log_message(self, format, *args):
        pass


def main():
    try:
        server = ExclusiveThreadingHTTPServer((HOST, PORT), AwcProxyHandler)
    except Exception as err:
        logger.critical("Failed to bind %s:%s: %s", HOST, PORT, err)
        raise

    logger.info("AWC proxy listening on http://%s:%s (BASE_DIR=%s)", HOST, PORT, BASE_DIR)
    try:
        server.serve_forever()
    except Exception as err:
        logger.critical("Server terminated unexpectedly: %s", err)
        raise
    finally:
        server.server_close()


if __name__ == "__main__":
    main()