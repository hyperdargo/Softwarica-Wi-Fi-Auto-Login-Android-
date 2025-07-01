import requests

url = "http://gateway.example.com/loginpages/userlogin.shtml"

# 🧠 Matching Headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://gateway.example.com/",
    "Connection": "keep-alive",
    "Referer": "http://gateway.example.com/loginpages/login.shtml?ReturnUrl=ZBu4bDqPWyeEeEZgUDdAb/dkVCN8KEu4MDe3V/dkUyewMAtMZA90b053",
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i"
}

# 🍪 Cookies — must match what the server expects
cookies = {
    "password": "Y292ZW50cnkyMDE5",  # base64 of 'coventry2019'
    "username": "softwarica@local",
    "Session": "65f46ff3b04bbae99a26bb3cffd2a209"
}

# 📦 Form Data
data = {
    "username": "softwarica",
    "password": "coventry2019",
    "accesscode": "",
    "vlan_id": "135"
}

try:
    response = requests.post(url, headers=headers, cookies=cookies, data=data, timeout=10)

    print("[+] Status Code:", response.status_code)
    print("[+] Response Text:\n")
    print(response.text)

except requests.exceptions.RequestException as err:
    print("[!] Request failed:", err)
