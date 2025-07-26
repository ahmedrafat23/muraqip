# main.py
from detector import detect_behavior
from alert_system import send_alert

def simulate_events():
    test_events = [
        "music",
        "normal_walk",
        "smoking",
        "unknown_person",
        "loud_noise",
        "praying",
        "littering"
    ]

    for event in test_events:
        alert_type, detail = detect_behavior(event)
        if alert_type != "Normal":
            send_alert(alert_type, detail)
        else:
            print(f"[INFO] Normal activity detected: {detail}")

if __name__ == "__main__":
    simulate_events()
