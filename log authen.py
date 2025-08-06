import re

def analyze_log(file_path):
    failed_logins = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Match lines with "Failed password" and extract the IP address
                match = re.search(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip = match.group(1)
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1

        # Print summary of failed attempts
        print("\n=== Failed Login Summary ===\n")
        for ip, count in failed_logins.items():
            alert = "🚨 ALERT: Possible brute-force attack!" if count >= 3 else ""
            print(f"[!] {ip} had {count} failed login attempt(s). {alert}")

        if not failed_logins:
            print("No failed login attempts found.")

    except FileNotFoundError:
        print(f"[ERROR] The file '{file_path}' was not found.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Try to use the file, but if not found, use embedded log data for testing
    import os
    log_path = "auth.log"
    if os.path.exists(log_path):
        analyze_log(log_path)
    else:
        print(f"[WARNING] The file '{log_path}' was not found. Using sample log data.")
        log_data = '''
Jul 31 08:32:05 ubuntu sshd[1010]: Failed password for invalid user admin from 192.168.1.22 port 22 ssh2
Jul 31 08:32:07 ubuntu sshd[1010]: Failed password for root from 192.168.1.22 port 22 ssh2
Jul 31 08:32:10 ubuntu sshd[1010]: Accepted password for root from 192.168.1.50 port 22 ssh2
'''
        # Slightly modify analyze_log to accept log text
        def analyze_log_text(log_text):
            failed_logins = {}
            for line in log_text.splitlines():
                match = re.search(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip = match.group(1)
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1
            print("\n=== Failed Login Summary ===\n")
            for ip, count in failed_logins.items():
                alert = "🚨 ALERT: Possible brute-force attack!" if count >= 3 else ""
                print(f"[!] {ip} had {count} failed login attempt(s). {alert}")
            if not failed_logins:
                print("No failed login attempts found.")
        analyze_log_text(log_data)
