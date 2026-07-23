from app.services.parser import parse_auth_log
from app.services.detector import analyze_events


events = parse_auth_log(
    "app/sample_logs/auth.log"
)

findings = analyze_events(events)


for finding in findings:
    print(finding)