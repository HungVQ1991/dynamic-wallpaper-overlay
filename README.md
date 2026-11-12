# Dynamic Weather Wallpaper

> **A Beautiful, Real-Time Animated Desktop Wallpaper for Windows**  
> *Automatically mirrors the weather, sun, and moon from the real world onto your desktop with realistic rain, wind, and water lighting effects—built to run silky smooth without slowing down your computer.*

---

## Table of Contents

1. [About the Wallpaper](#about-the-wallpaper)
2. [What Makes It Special](#what-makes-it-special)
   - [Live Weather Outside Your Window](#live-weather-outside-your-window)
   - [Real Sun and Moon Cycles](#real-sun-and-moon-cycles)
   - [Living Water, Rain, and Wind Effects](#living-water-rain-and-wind-effects)
   - [Battery-Friendly & Silky-Smooth Performance](#battery-friendly--silky-smooth-performance)
3. [Simple Installation Guide (For Everyone)](#simple-installation-guide-for-everyone)
   - [Step 0: How to Download from GitHub](#step-0-how-to-download-from-github)
   - [Method 1: Lively Wallpaper (Free & Easiest - Recommended)](#method-1-lively-wallpaper-free--easiest---recommended)
   - [Method 2: Wallpaper Engine (Steam)](#method-2-wallpaper-engine-steam)
   - [Method 3: Direct Fullscreen in Any Browser](#method-3-direct-fullscreen-in-any-browser)
4. [How to Customize Your Settings](#how-to-customize-your-settings)
   - [Step-by-Step: Changing Settings in Notepad](#step-by-step-changing-settings-in-notepad)
   - [Simple Parameter Reference Table](#simple-parameter-reference-table)
5. [Interactive Control Studio (`controls.html`)](#interactive-control-studio-controlshtml)
   - [On-Screen Sliders & Real-Time Controls](#on-screen-sliders--real-time-controls)
   - [Keyboard Shortcut Reference](#keyboard-shortcut-reference)
6. [Frequently Asked Questions & Troubleshooting](#frequently-asked-questions--troubleshooting)
7. [License & Credits](#license--credits)

---

## About the Wallpaper

**Dynamic Weather Wallpaper** turns your Windows desktop background into a living, responsive window to the outdoors. 

Instead of showing a repeating video loop, the wallpaper actively looks up the actual weather at your chosen city and simulates the natural light throughout the day and night:
* When it rains in your city, gentle raindrops fall on your screen and create ripples on the water.
* As the sun sets, warm golden rays sweep across the landscape.
* At night, the sky fills with stars and the scene is lit by the current real-world phase of the moon.

Everything runs directly on your computer's graphics card, consuming virtually no battery power and leaving your computer completely free for gaming, school, or work.

---

## What Makes It Special

### Live Weather Outside Your Window
* **Zero Setup Required:** Works right out of the box. Automatically checks the real weather for your location every 10 minutes without needing any accounts, subscriptions, or API keys.
* **Smart Weather Matching:** Changes cloudiness, wind speed, and rain intensity to match what is happening outside your home in real life.
* **Always Ready:** If your internet connection drops, the wallpaper keeps running smoothly using gentle default weather until you are back online.

### Real Sun and Moon Cycles
* **Natural 24-Hour Day:** Smoothly transitions from soft morning dawn to bright daytime, rich sunset colors, and deep midnight blue based on your local time.
* **True Moon Phases:** Tracks the actual phase of the moon night by night. On full moon nights, the landscape glows bright and colorful under lunar light; during crescent or new moons, the night stays softly dim.
* **Golden Sunrise & Sunset Beams:** Warm beams of sunlight naturally burst across the landscape around dawn and dusk, automatically softening when clouds roll in.

### Living Water, Rain, and Wind Effects
* **Multi-Layered Rain:** Rain falls in two depths—soft background drops and clearer foreground streaks—tilting naturally with the blowing wind.
* **Pond Ripples:** Every raindrop that touches the water surface creates realistic expanding ripples.
* **Sunlight Under Water:** Bright dancing sunlight patterns shimmer along the shallow pond bed during clear daylight hours.
* **Water Surface Sparkles:** Sunlight and moonlight reflect off the moving water surface with soft, natural glints.
* **Soft Morning Mist:** A gentle, quiet lake fog appears over the water surface around sunrise, naturally clearing up as the day warms.
* **Twinkling Starry Nights:** Clear nights reveal a sky of twinkling stars, which naturally hide when clouds or rain gather.

### Battery-Friendly & Silky-Smooth Performance
* **Zero Slowdowns:** Uses less than 1% of your computer's processor (CPU), so your apps, games, and browsing remain fast and responsive.
* **Smart Auto-Pause:** When you are playing a game or have a window maximized covering your desktop, the wallpaper automatically pauses completely to save battery life.
* **Ultra-Smooth 60–144 FPS:** Designed to match your monitor's highest refresh rate without stuttering or memory buildup.
* **Fits Any Screen:** Looks crisp on any display, from standard laptop screens to 4K and ultrawide monitors.

---

## Simple Installation Guide (For Everyone)

You do **not** need any programming knowledge to use this wallpaper. Follow the simple steps below:

### Step 0: How to Download from GitHub

If you are viewing this project on GitHub and want to save it to your computer:

#### Easy 1-Click Download (No Tools Needed)
1. Scroll to the top of this GitHub repository page.
2. Click the bright green **`<> Code`** button (located near the top-right of the file list).
3. In the drop-down menu that appears, click **`Download ZIP`**.
4. Once the download finishes, open your computer's **Downloads** folder, right-click the downloaded `.zip` file, and choose **`Extract All...`** → click **`Extract`**.
5. You now have a complete, ready-to-use folder containing `index.html`, `controls.html`, `wallpaper.jpg`, and all project files! Move this folder anywhere you like (for example, into your `Documents` folder).

*(For users with Git installed, you can also simply run: `git clone https://github.com/<your-username>/<repo-name>.git`)*

---

### Method 1: Lively Wallpaper (Free & Easiest - Recommended)

[Lively Wallpaper](https://rocksdanister.github.io/lively/) is a 100% free, safe, open-source animated wallpaper manager made for Windows 10 and 11.

1. **Install Lively Wallpaper:**
   - Open the **Microsoft Store** on your Windows PC, search for **Lively Wallpaper**, and click **Install** (or download it free from their official website).
2. **Open the App:**
   - Launch Lively Wallpaper from your Windows Start Menu.
3. **Add Your Wallpaper:**
   - Click the **`+ Add Wallpaper`** button in the top-right corner.
   - Click **`Browse`** and navigate to your wallpaper folder:  
     `C:\Users\PC\Documents\WeatherWallpaper\`
   - Choose:
     - **`index.html`** for a clean, pure live background without any buttons on screen.
     - **`controls.html`** if you prefer having an interactive settings panel in the corner of your desktop.
   - Click **`Open`**.
4. **Enjoy:**
   - Enter any name you like (e.g., *My Weather Wallpaper*) and click **`OK`**.
   - Your desktop is now live!

---

### Method 2: Wallpaper Engine (Steam)

If you already use [Wallpaper Engine](https://store.steampowered.com/app/431960/Wallpaper_Engine/) on Steam:

1. Open **Wallpaper Engine**.
2. Click **`Wallpaper Editor`** (or right-click the Wallpaper Engine tray icon by your clock and choose *Create Wallpaper*).
3. Select **`Create New Wallpaper`** → choose **`New Web Wallpaper`**.
4. In the file browser, click on:  
   `C:\Users\PC\Documents\WeatherWallpaper\index.html`
5. Name it *Dynamic Weather Wallpaper* and set your preferred screen resolution.
6. Click **`File`** → **`Save`**, then click **`Apply`**.

---

### Method 3: Direct Fullscreen in Any Browser

You can also run this on a secondary monitor or TV screen without installing any third-party app:

1. Double-click **`index.html`** or **`controls.html`** to open it in Chrome, Edge, Brave, or Firefox.
2. Press **`F11`** on your keyboard to enter borderless Fullscreen mode.
3. If using `controls.html`, you can press the **`4`** key at any time to hide or show the controls panel.

---

## How to Customize Your Settings

At the very top of both [`index.html`](file:///C:/Users/PC/Documents/WeatherWallpaper/index.html) and [`controls.html`](file:///C:/Users/PC/Documents/WeatherWallpaper/controls.html), there is an easy-to-read list of settings. You can change your city, lock the time to night, make it constantly rainy, or turn up the sparkles.

### Step-by-Step: Changing Settings in Notepad

1. Open your wallpaper folder in Windows File Explorer:  
   `C:\Users\PC\Documents\WeatherWallpaper\`
2. Right-click on **`index.html`** (or **`controls.html`**) and select **Open with** → **Notepad**.
3. Look at the top of the file (lines 38 to 65). You will see simple lines like this:

```javascript
        const LATITUDE = 21.0285;
        const LONGITUDE = 105.8542;
        const WEATHER_UPDATE_INTERVAL_MINUTES = 10;

        const SHOW_HUD = true; // controls.html only (true: show panel, false: hide)
        const SCALE_MODE = 0;

        const TIME_MODE = 0;
        const MANUAL_HOUR = 12.0;

        const CLOUD_MODE = 0;
        const MANUAL_CLOUD = 0.50;

        const RAIN_MODE = 0;
        const MANUAL_RAIN = 0.0;

        const WIND_MODE = 0;
        const MANUAL_WIND_SPEED_KMH = 10.0;
        const MANUAL_WIND_DEG = 45.0;

        const MIST_MODE = 0;
        const MANUAL_MIST = 0.0;

        const MOON_BOOST = 1.0;
        const CAUSTIC_BOOST = 1.0;
        const RAY_BOOST = 1.0;
        const GLINT_BOOST = 1.0;
        const STAR_BOOST = 1.0;
        const RIPPLE_BOOST = 1.0;
```

4. Simply change the numbers to whatever you like. For example:
   - **Want your city's weather?** Replace `LATITUDE` and `LONGITUDE` with your city's coordinates.
   - **Want constant cozy night?** Set `TIME_MODE = 2;` and `MANUAL_HOUR = 23.0;`.
   - **Want constant heavy rain?** Set `RAIN_MODE = 1;`.
   - **Want brighter sun rays and sparkles?** Set `RAY_BOOST = 1.5;` and `GLINT_BOOST = 1.5;`.
5. Press **`Ctrl + S`** to save your file.
6. Refresh your wallpaper or reload the page in your browser. The new look appears immediately!

---

### Simple Parameter Reference Table

| Setting | Default | Range | What It Does & How to Use It |
| :--- | :--- | :--- | :--- |
| `LATITUDE` / `LONGITUDE` | `21.0285` / `105.8542` | Any city coordinates | Your geographic location. Defaults to Hanoi. (See FAQ below for how to find your city's coordinates in 10 seconds). |
| `WEATHER_UPDATE_INTERVAL_MINUTES` | `10` | `1` to `60` minutes | How often the wallpaper checks the real-world weather forecast. |
| `SHOW_HUD` *(controls.html)* | `true` | `true` / `false` | Sets whether the visual on-screen control box is visible when the wallpaper opens. |
| `SCALE_MODE` | `0` | `0` or `1` | `0`: **Fit** (keeps the full original picture with clean black side borders); `1`: **Fill** (zooms in slightly to fill your whole screen with no borders). |
| `TIME_MODE` | `0` | `0`, `1`, `2` | `0`: Follows your computer's real clock; `1`: Fast showcase mode (a full 24-hour cycle every 15 seconds); `2`: Locks the clock to `MANUAL_HOUR`. |
| `MANUAL_HOUR` | `12.0` | `0.0` to `24.0` | The fixed hour of the day when `TIME_MODE = 2` (e.g., `6.0` for sunrise, `18.0` for sunset, `23.0` for late night). |
| `CLOUD_MODE` | `0` | `0` or `1` | `0`: Uses real-world clouds from the weather forecast; `1`: Locks clouds to `MANUAL_CLOUD`. |
| `MANUAL_CLOUD` | `0.50` | `0.0` to `1.0` | How cloudy the sky is when `CLOUD_MODE = 1` (`0.0` = completely sunny, `1.0` = heavy overcast). |
| `RAIN_MODE` | `0` | `0`, `1`, `2` | `0`: Uses real rain from the weather forecast; `1`: Constant storm (20 mm/h); `2`: Custom rain using `MANUAL_RAIN`. |
| `MANUAL_RAIN` | `0.0` | `0.0` to `20.0` mm/h | Rain strength when `RAIN_MODE = 2` (`0.0` = dry, `2.5` = light drizzle, `10.0` = heavy shower, `20.0` = storm). |
| `WIND_MODE` | `0` | `0` or `1` | `0`: Uses real wind from the weather forecast; `1`: Custom wind using the two settings below. |
| `MANUAL_WIND_SPEED_KMH` | `10.0` | `0.0` to `40.0` km/h | Wind speed. Makes raindrops tilt and drift sideways faster. |
| `MANUAL_WIND_DEG` | `45.0` | `0` to `360` degrees | Wind direction on a compass (0° = North, 90° = East, 180° = South, 270° = West). |
| `MIST_MODE` | `0` | `0` or `1` | `0`: Natural morning mist appears automatically around dawn; `1`: Custom mist using `MANUAL_MIST`. |
| `MANUAL_MIST` | `0.0` | `0.0` to `1.0` | Thickness of the morning lake fog (`0.0` = clear, `1.0` = thick fog). |
| `MOON_BOOST` | `1.0` | `0.0` to `3.0` | Brightness of the moonlight on the landscape at night (`1.0` = natural, `2.0` = brilliant moonlight). |
| `CAUSTIC_BOOST` | `1.0` | `0.0` to `2.0` | Brightness of the dancing sunlight patterns at the bottom of the shallow pond. |
| `RAY_BOOST` | `1.0` | `0.0` to `2.0` | Visibility of golden sunlight beams during sunrise and sunset. |
| `GLINT_BOOST` | `1.0` | `0.0` to `2.0` | Brightness of sparkles reflecting off the moving water surface. |
| `STAR_BOOST` | `1.0` | `0.0` to `2.0` | Brightness and quantity of twinkling night stars. |
| `RIPPLE_BOOST` | `1.0` | `0.0` to `2.0` | Size and visibility of water ripples created by raindrops. |

---

## Interactive Control Studio (`controls.html`)

If you want to experiment with different visual looks on the fly without editing text files, open [`controls.html`](file:///C:/Users/PC/Documents/WeatherWallpaper/controls.html) in your browser.

### On-Screen Sliders & Real-Time Controls
* **Live Status Box:** In the upper corner, you can see your connection status, your local time, and the current moon phase (like *First Quarter* or *Full Moon*).
* **Live Sliders:** Drag sliders to instantly change the hour of the day, cloud cover percentage, rain strength, wind speed, fog thickness, or effect brightness.
* **Instant Switching:** As soon as you drag a slider, it switches that setting to manual so you can preview it immediately.

### Keyboard Shortcut Reference

You can also use quick single-key shortcuts on your keyboard:

| Key | What It Does |
| :---: | :--- |
| **`1`** | **Cycle Rain:** Switches between Live Real Rain → Heavy Storm (20 mm/h) → Manual. |
| **`2`** | **Cycle Time:** Switches between Real Time → Fast 15-Second Day/Night Loop → Manual. |
| **`4`** | **Hide/Show Panel:** Toggles the entire settings box on or off for clean viewing. |
| **`5`** | **Cycle Mist:** Toggles between Natural Sunrise Mist and Manual Mist. |
| **`6`** | **Cycle Clouds:** Toggles between Overcast (96%), Sunny (5%), and Live Forecast. |
| **`7`** | **Cycle Wind:** Toggles between Live Real Wind and Manual Wind. |
| **`8`** | **Boost Moon:** Toggles moonlight between Normal (`1.0x`) and Extra Bright (`1.6x`). |
| **`C`** | **Toggle Underwater Sun:** Turns the underwater dancing sunlight patterns on or off. |
| **`R`** | **Toggle Sun Rays:** Turns golden hour sunrise/sunset beams on or off. |
| **`G`** | **Toggle Sparkles:** Turns sparkling water reflections on or off. |
| **`S`** | **Toggle Stars:** Turns twinkling night stars on or off. |
| **`W`** | **Toggle Ripples:** Turns rain pond ripples on or off. |

---

## Frequently Asked Questions & Troubleshooting

#### How do I find the coordinates for my hometown?
1. Open [Google Maps](https://maps.google.com) on your computer or phone.
2. Right-click (or tap and hold on mobile) on your city or neighborhood.
3. A small box will appear showing two numbers separated by a comma (for example: `40.7128, -74.0060`).
4. Click on the numbers to copy them. Paste the first number into `LATITUDE` and the second number into `LONGITUDE`.

#### The wallpaper has black bars on the sides. How do I make it fill my screen?
Open `index.html` in Notepad, look for `const SCALE_MODE = 0;`, and change it to:
```javascript
const SCALE_MODE = 1;
```
This tells the wallpaper to seamlessly zoom in and fill your entire display with no black bars.

#### The weather does not match what I see out my window right now.
Global weather satellite data updates in regular cycles. If rain just started a minute ago, the online weather station may take a few minutes to report it. You can either wait for the next automatic update, decrease `WEATHER_UPDATE_INTERVAL_MINUTES = 5;`, or press the **`1`** key to trigger rain manually.

#### Does this use a lot of internet data?
No. It only downloads a tiny text forecast (less than half of a single kilobyte) once every 10 minutes. It uses essentially zero network data.

#### Will this slow down my computer while I play video games?
No. When you play a game or open any window full screen, Windows informs the wallpaper to pause its drawing entirely. It uses 0% CPU and 0% GPU while you are gaming.

---

## License & Credits

* **Weather Service:** Live weather forecasts provided freely by the open-access [Open-Meteo Weather API](https://open-meteo.com/).
* **License:** Released freely under the **MIT License**. You are welcome to customize, share, and enjoy this wallpaper on as many personal computers as you like!
