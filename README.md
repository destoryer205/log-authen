 SSH Log Analyzer – Failed Login Detection

 Description

This Python script analyzes SSH authentication logs (`auth.log`) to detect and report failed login attempts from various IP addresses. It flags possible brute-force attacks when an IP has three or more failures. If the log file isn't found, it uses embedded sample data for testing purposes.

This tool is useful for security monitoring, basic intrusion detection, and practicing log file analysis.

---

 How It Works

- Scans for lines containing `Failed password`.
- Extracts the IP address from each failed login attempt.
- Counts and groups failures by IP address.
- Flags IPs with **3 or more failed attempts** as potential brute-force attackers.
- Saves the summary to a text file in the `/output` folder.

---

 Use Case

This project was built as part of my journey into cybersecurity and log analysis. It's ideal for:
- Practicing **regex and file handling** in Python.
- Learning how to **analyze real-world system logs**.
- Developing tools for **basic intrusion detection**.
- Showing security-focused skills in a **portfolio or internship application**.

---



