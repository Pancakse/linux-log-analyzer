import re

def parse_log(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    entries = []
    for line in lines:
        if "sshd" in line and ("Failed password" in line or "Accepted password" in line):
            entries.append(line.strip())
    return entries
