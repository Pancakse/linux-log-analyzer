def generate_report(failed_logins, brute_force_attempts):
    print("\n--- Security Event Report ---")
    print(f"Total Failed Logins: {len(failed_logins)}")
    print("\nPotential Brute Force Attempts:")
    for ip, count in brute_force_attempts.items():
        print(f"  {ip} -> {count} failed attempts")
