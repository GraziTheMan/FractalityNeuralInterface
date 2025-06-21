# cognitive_timeline_serializer.py
# Serializes neural symbolic events into a persistent timeline structure

import json
from datetime import datetime

class CognitiveTimeline:
    def __init__(self):
        self.timeline = []

    def log_event(self, signal_type, node_id, label):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "signal": signal_type,
            "node_id": node_id,
            "label": label
        }
        self.timeline.append(entry)

    def export(self, path="timeline.json"):
        with open(path, "w") as f:
            json.dump(self.timeline, f, indent=2)
        print(f"🗂 Timeline saved to {path}")

if __name__ == "__main__":
    timeline = CognitiveTimeline()
    timeline.log_event("beta_burst", "node_123", "Flash of Genius")
    timeline.log_event("theta_surge", "node_456", "Dream Fragment")
    timeline.export()
