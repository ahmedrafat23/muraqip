# detector.py

def detect_behavior(event):
    """Simulate behavior analysis based on incoming events."""
    behavior_events = ["music", "smoking", "littering"]
    sound_events = ["loud_noise"]
    person_events = ["unknown_person"]

    if event in behavior_events:
        return "Behavior Alert", event
    elif event in sound_events:
        return "Sound Alert", event
    elif event in person_events:
        return "Person Alert", event
    else:
        return "Normal", event
