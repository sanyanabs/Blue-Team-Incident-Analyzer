from app.services.parser import parse_auth_log


events = parse_auth_log(
    "app/sample_logs/auth.log"
)


for event in events:
    print(event)