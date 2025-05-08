from analyzer.parser import parse_log
from analyzer.detector import detect_brute_force, detect_failed_logins
from analyzer.report import generate_report

def main():
    log_path = "logs/sample_auth.log"
    entries = parse_log(log_path)

    failed_logins = detect_failed_logins(entries)
    brute_force_attempts = detect_brute_force(failed_logins)

    generate_report(failed_logins, brute_force_attempts)

if __name__ == "__main__":
    main()
