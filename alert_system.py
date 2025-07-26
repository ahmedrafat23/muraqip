# alert_system.py
import json
from datetime import datetime

def send_alert(alert_type, detail):
    print(f"[ALERT] {alert_type} detected: {detail}")
    log_event(alert_type, detail)

def log_event(alert_type, detail):
    log = {
        "timestamp": datetime.now().isoformat(),
        "alert_type": alert_type,
        "detail": detail
    }

    try:
        with open("event_log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(log)

    with open("event_log.json", "w") as f:
        json.dump(data, f, indent=4)
