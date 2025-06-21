# realtime_receiver_stub.py
# Simulates a WebSocket or BLE receiver for neural JSON payloads

import asyncio
import json
import random

MOCK_EVENTS = [
    {"signal": "alpha_peak", "intensity": 0.7},
    {"signal": "beta_burst", "intensity": 0.9},
    {"signal": "theta_surge", "intensity": 0.65},
    {"signal": "p300_response", "intensity": 0.85}
]

async def simulate_receiver():
    print("Starting Neural Event Receiver Stub...")
    while True:
        event = random.choice(MOCK_EVENTS)
        payload = {
            "type": "neural_event",
            "signal": event["signal"],
            "intensity": event["intensity"],
            "duration_ms": random.randint(200, 700),
            "timestamp": "2025-06-21T00:00:00Z",
            "mapped_action": {
                "action_type": "highlight_cluster",
                "target_node_id": "node_" + str(random.randint(1000, 9999)),
                "strength": event["intensity"]
            }
        }
        print("Received:", json.dumps(payload, indent=2))
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(simulate_receiver())
