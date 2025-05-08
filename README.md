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

## 🚀 How to Use

1. Clone this repo:
   ```bash
   git clone https://github.com/Pancakse/linux-log-analyzer.git
   cd linux-log-analyzer
2. Install dependencies:
pip install -r requirements.txt
3. Run the analyzer:
python main.py

## 📂 Log File

Replace logs/sample_auth.log with real log files from:

/var/log/auth.log

## 🧰 Requirements

Python 3.6+

No external libraries required (standard Python only)
