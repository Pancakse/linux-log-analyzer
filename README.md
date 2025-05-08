# 🛡️ Linux Log Analyzer

A Python CLI tool that analyzes `/var/log/auth.log` for:

- Failed login attempts
- Brute force detection based on IP
- Simple event report output

## 🧪 Sample Output
--- Security Event Report ---
Total Failed Logins: 16

Potential Brute Force Attempts:
192.168.0.12 -> 7 failed attempts
10.0.0.3 -> 5 failed attempts
