# 🌐 WiFi Captive Portal Auto-Login

A Python automation script designed to automatically log into a specific WiFi captive portal (192.168.12.2) when connected to recognized hostel or college networks. It uses Selenium to handle credential injection and status verification.

## ✨ Features
- **SSID Detection:** Automatically identifies the currently connected WiFi network using system commands (`netsh`).
- **Selective Activation:** Only attempts to log in if the connected network is found in a predefined whitelist (e.g., `mvhstl`, `MVCTAE`, etc.).
- **Multi-Credential Support:** Iterates through a dictionary of usernames and passwords until a successful login is achieved.
- **Real-time Verification:** Reads the response from the login page to confirm success before terminating.

## 🛠️ Prerequisites
- **Python 3.x**
- **Google Chrome** installed on the system.
- **Selenium Library:**
  ```bash
  pip install selenium
