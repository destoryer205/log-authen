# SSH Log Analyzer – Failed Login Detection

##  Description

This Python script analyzes SSH authentication logs (`auth.log`) to detect and report failed login attempts from various IP addresses. It flags possible brute-force attacks when an IP has three or more failures. If the log file isn't found, it uses embedded sample data for testing purposes.

This tool is useful for security monitoring, basic intrusion detection, and practicing log file analysis.

---

##  How It Works

- Scans for lines containing `Failed password`.
- Extracts the IP address from each failed login attempt.
- Counts failures per IP and flags IPs with 3+ failures as possible brute-force attackers.
- Provides summary output.

---

##  Use Case

This project was built as part of my journey into cybersecurity and log analysis. It's ideal for:
- Practicing **regex and file handling** in Python.
- Learning about basic log-based intrusion detection.
- Building your own security tools.

---

##  Getting Started

1. Clone this repo:  
   ```bash
   git clone https://github.com/destoryer205/log-authen.git
   cd log-authen
   ```
2. Run the script (replace `your-log-path` with the path to your `auth.log`):  
   ```bash
   python3 log_analyzer.py /var/log/auth.log
   ```
   If no log is found, the script uses sample data.

---

##  Sample Output

```
Failed login attempts:
192.168.0.10: 5 [!! Possible brute-force attacker]
203.0.113.5: 2
...
```

---

##  License

MIT

## 👤 Author

destoryer205
