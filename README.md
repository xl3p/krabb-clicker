# 🦀 Krabb-Clicker
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/Flet-0.28.3-00599C?logo=python&logoColor=white)](https://flet.dev/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.54-3776AB?logo=python&logoColor=white)](https://pypi.org/project/PyAutoGUI/)
[![Pynput](https://img.shields.io/badge/Pynput-1.7.8-FF9800?logo=python&logoColor=white)](https://pypi.org/project/pynput/)
[![Platform](https://img.shields.io/badge/Windows-10%2F11-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/en-us/windows)
[![Platform](https://img.shields.io/badge/Linux-glibc%202.39+-FCC624?logo=linux&logoColor=black)](https://rus-linux.net/MyLDP/algol/glibc-version.html)

A lightweight, customizable autoclicker with a modern GUI built with Flet. Supports both mouse buttons and keyboard keys with configurable click intervals.

## ✨ Features

- **Multiple Click Types** – Supports left, middle, right mouse buttons and any keyboard key
- **Configurable Click Speed** – Set custom gap time between clicks (0 to 99999.99999 seconds)
- **Start/Stop Hotkey** – Bind any keyboard or mouse button to toggle clicking
- **Frameless Window** – Clean, minimal interface with custom title bar
- **Cross-Platform** – Runs on Windows and Linux

## 📋 Requirements

### Windows 10/11 (64-bit)

### Linux
- glibc 2.39+
#### To see glibc version
``` bash
ldd --version
```

## 🚀 Installation

### From Release (Pre-built)

1. Download the appropriate archive for your operating system from [the Releases page](https://github.com/xl3p/krabb-clicker/releases)

2. Extract `.zip` and run krabb-clicker

## 🎮 Usage

### Setting Up

1. Click Key – Click the "key" button, then press any keyboard key or mouse button to set it as the clicking key

2. Start/Stop Key – Click the "start key" button and press a key to bind the toggle hotkey

3. Gap Time – Enter the delay between clicks in seconds (e.g., 0.5 for 500ms)

### Controls

1. Start Listener – Click to enable the start/stop hotkey monitoring

2. Stop Listener – Disable the hotkey monitoring

3. Minimize – Minimize to system tray

4. Fullscreen – Toggle fullscreen mode

### How It Works

1. Configure your click key, start key, and gap time

2. Press "Start Listener" to activate hotkey monitoring

3. Press your configured start key to begin/stop autoclicking

4. The autoclicker will repeatedly press your chosen key at the specified interval

### 🔧 Dependencies

1. flet – Modern GUI framework

2. pyautogui – Mouse and keyboard automation

3. pynput – Keyboard and mouse input monitoring

### ⚠️ Disclaimer

This tool is intended for legitimate automation purposes only. Users are responsible for complying with the terms of service of any applications or games they use this with. The developer assumes no liability for misuse.

### 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

### 🤝 Contributing

Contributions are welcome! Feel free to:

Report bugs

Suggest features

### Feedback
Made with 🦀 by [xl3pp](xl3p)

My [telegram](https://t.me/xlpp3)
