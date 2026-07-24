def detect_auth_events(events):
    findings = []
    failed_attempts = {}

    for event in events:

        if event.get("event_type") == "successful_login":
            findings.append({
                "title": "Successful SSH Login Detected",
                "severity": "Low",
                "description": (
                    f"User {event.get('user')} successfully authenticated "
                    f"from source IP {event.get('source_ip')}."
                ),
                "impact": (
                    "If the login was unauthorized, an attacker may have gained "
                    "access to the system."
                ),
                "recommendation": (
                    "Verify that the login was performed by an authorized user "
                    "and confirm the source IP is expected."
                ),
                "response_action": (
                    "Review user activity, validate account ownership, and "
                    "investigate any suspicious access."
                )
            })
            

        elif event.get("event_type") == "sudo_command":
            findings.append({
                "title": "Privileged Command Execution Detected",
                "severity": "High",
                "description": (
                    f"User {event.get('user')} executed a command with elevated "
                    "privileges using sudo."
                ),
                "impact": (
                    "Unauthorized privileged activity could allow an attacker "
                    "to modify system settings, access sensitive data, or "
                    "perform further compromise."
                ),
                "recommendation": (
                    "Review the executed command and confirm the activity "
                    "was authorized."
                ),
                "response_action": (
                    "Investigate the user account, review audit logs, and "
                    "escalate to the security team if unauthorized."
                )

            })

        elif event.get("event_type") == "failed_login":

            ip = event.get("source_ip")

            if ip:
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    for ip, count in failed_attempts.items():

        if count >= 3:

            findings.append({
                "title": "Multiple Failed Login Attempts Detected",
                "severity": "Medium",
                "description": (
                    f"{count} failed login attempts were detected "
                    f"from IP address {ip}."
                ),
                "impact": (
                    "The activity may indicate a brute-force attempt "
                    "to gain unauthorized access."
                ),
                "recommendation": (
                    "Review authentication logs and investigate the "
                    "source IP."
                ),
                "response_action": (
                    "Block the IP address if malicious activity is "
                    "confirmed and reset affected credentials."
                )
            })

    return findings