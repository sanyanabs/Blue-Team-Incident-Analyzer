def analyze_events(events):
    findings = []

    for event in events:

        # Successful SSH login
        if event.get("event_type") == "successful_login":
            findings.append({
                "finding": "Successful SSH login detected",
                "severity": "Informational",
                "user": event.get("user"),
                "source_ip": event.get("source_ip"),
                "recommendation": "Verify login activity is authorized"
            })


        # Privileged command execution
        elif event.get("event_type") == "sudo_command":
            findings.append({
                "finding": "Privileged command execution detected",
                "severity": "Medium",
                "user": event.get("user"),
                "recommendation": "Review administrative activity"
            })


        # Failed authentication
        elif event.get("event_type") == "failed_login":
            findings.append({
                "finding": "Failed authentication attempt detected",
                "severity": "Medium",
                "source_ip": event.get("source_ip"),
                "recommendation": "Investigate repeated authentication failures"
            })


    return findings