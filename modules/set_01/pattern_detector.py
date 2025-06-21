# pattern_detector.py
# Simulates EEG pattern detection and emits FBIP-compliant JSON

import json
import random
from datetime import datetime

def generate_mock_event():
    patterns = ['alpha_peak', 'beta_burst', 'theta_surge', 'p300_response', 'gamma_sync']
    pattern = random.choice(patterns)
    event = {
        "type": "neural_event",
        "signal": pattern,
        "intensity": round(random.uniform(0.4, 1.0), 2),
        "duration_ms": random.randint(100, 800),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "mapped_action": {
            "action_type": "generate_node" if pattern == "beta_burst" else "highlight_cluster",
            "target_node_id": "node_" + str(random.randint(1000, 9999)),
            "strength": round(random.uniform(0.5, 1.0), 2)
        }
    }
    return json.dumps(event, indent=2)

if __name__ == "__main__":
    print(generate_mock_event())
