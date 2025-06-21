# temporal_cognition_tracker.py
# Tracks changes in neural signal patterns over time to generate symbolic trends

import time
from collections import deque

class TemporalCognitionTracker:
    def __init__(self, window_size=5):
        self.window = deque(maxlen=window_size)

    def record_event(self, signal_type):
        timestamp = time.time()
        self.window.append((signal_type, timestamp))
        print(f"Recorded: {signal_type} @ {timestamp}")
        self.analyze_temporal_pattern()

    def analyze_temporal_pattern(self):
        if len(self.window) < 3:
            return
        signals = [e[0] for e in self.window]
        print(f"Recent pattern: {signals}")
        if signals[-3:] == ["theta_surge", "alpha_peak", "gamma_sync"]:
            print("🔮 Insight Sequence Detected!")

if __name__ == "__main__":
    tracker = TemporalCognitionTracker()
    tracker.record_event("theta_surge")
    tracker.record_event("alpha_peak")
    tracker.record_event("gamma_sync")
