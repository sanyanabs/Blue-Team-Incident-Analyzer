import re


def parse_auth_log(file_path):
    events = []

    with open(file_path, "r") as file:
        for line in file:
            event = parse_line(line)

            if event:
                events.append(event)

    return events


def parse_line(line):
    event = {
        "raw_log": line.strip()
    }

    # Extract timestamp and hostname
    pattern = r"^(.*?) (\w+) "

    match = re.search(pattern, line)

    if match:
        event["timestamp"] = match.group(1)
        event["hostname"] = match.group(2)

    # Detect SSH successful login
    if "Accepted" in line and "sshd" in line:
        event["event_type"] = "successful_login"

        user = re.search(r"for (\w+)", line)
        ip = re.search(r"from ([0-9.]+)", line)

        if user:
            event["user"] = user.group(1)

        if ip:
            event["source_ip"] = ip.group(1)


    # Detect sudo activity
    elif "sudo:" in line:
        event["event_type"] = "sudo_command"

        user = re.search(r"sudo: (\w+)", line)

        if user:
            event["user"] = user.group(1)


    # Detect failed login
    elif "Failed password" in line:
        event["event_type"] = "failed_login"

        ip = re.search(r"from ([0-9.]+)", line)

        if ip:
            event["source_ip"] = ip.group(1)


    else:
        event["event_type"] = "system_event"


    return event