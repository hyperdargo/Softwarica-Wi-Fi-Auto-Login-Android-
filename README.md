
---

## 📶 Softwarica Wi-Fi Auto Login (Android)
![GitHub](https://img.shields.io/badge/license_-AnkitGupta-red)

This is a simple Python script designed to **automatically log in to the Softwarica College Wi-Fi** gateway. It simulates a browser login request using the `requests` library.

---

### 📱 Requirements

* **Android device**
* **[Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)** (Python IDE for Android)
* Internet connection via LR/STWCU Wi-Fi (you must be connected)

---

### 🛠 Setup Instructions

#### 1. **Install Pydroid 3**

* Download from the [Play Store](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3).
* Open the app.

#### 2. **Install Required Module**

* Tap on the `≡` **menu** in the top-left corner.
* Go to **PIP** (Python Package Manager).
* Search for:

  ```
  requests
  ```
* Tap **Install**.

Alternatively, you can open the **terminal** in Pydroid 3 and type:

```bash
pip install requests
```

---

### ▶️ How to Use

1. **Connect to the LR5 / LR-XX / STWCU\_LR Wi-Fi** from your Android phone.
2. Open **Pydroid 3**.
3. Paste the Python script into a new file.
4. Tap the **Play** (▶️) button to run the script.
5. If credentials and session are valid, it will authenticate you to the college gateway and grant access.

---

### 🔐 Script Overview

* **Target URL:** `http://gateway.example.com/loginpages/userlogin.shtml`
* **Data Sent:**

  * `username`: `softwarica`
  * `password`: `coventry2019`
  * `vlan_id`: `135`
* **Headers and cookies** are set to mimic a real Firefox browser request for successful gateway interaction.

---

### ⚠️ Note

* The script uses hardcoded credentials and a session ID. If login fails:

  * The session might have expired — regenerate it via the browser and update the cookie.
  * The password may have changed — verify from college.
* This script only logs you in — you must already be **connected to the Wi-Fi** manually via system settings.

---

### 📄 License

This script is for **educational use only**. Do not distribute or misuse it on unauthorized networks.

---
## 🙋 About the Author

I'm **Ankit Gupta** (aka **Dargo Tamber**), a developer and ethical hacker based in Kathmandu, Nepal.
Currently studying at **Softwarica College**, I build tools that solve practical problems — like this Wi-Fi connector made specifically for students.

📫 Contact me at: [ankitstudentid@gmail.com](mailto:ankitstudentid@gmail.com)
🌐 GitHub: [@hyperdargo](https://github.com/hyperdargo)

---
