from collections import defaultdict
import re

def detect_failed_logins(log_entries):
    failed = [line for line in log_entries if "Failed password" in line]
    return failed

def detect_brute_force(failed_logins, threshold=5):
    ip_counts = defaultdict(int)
    ip_regex = re.compile(r"from (\d{1,3}(?:\.\d{1,3}){3})")

    for entry in failed_logins:
        match = ip_regex.search(entry)
        if match:
            ip_counts[match.group(1)] += 1

    return {ip: count for ip, count in ip_counts.items() if count >= threshold}
