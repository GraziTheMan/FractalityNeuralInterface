# device_sync_manager.py
# Handles state syncing across multiple Fractality-enabled devices

import json
import uuid

class DeviceSyncManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.sync_id = str(uuid.uuid4())
        self.device_registry = {}

    def register_device(self, device_name, capabilities):
        self.device_registry[device_name] = {
            "capabilities": capabilities,
            "last_sync": None
        }
        print(f"🔗 Device registered: {device_name}")

    def sync_state(self, state_payload):
        for device, info in self.device_registry.items():
            print(f"Syncing to {device}: {json.dumps(state_payload)}")
            info["last_sync"] = state_payload["timestamp"]

# Example usage
if __name__ == "__main__":
    import datetime
    sync = DeviceSyncManager("grazi")
    sync.register_device("desktop_node", ["visual", "neural"])
    sync.register_device("headband_v1", ["EEG"])
    sync.sync_state({
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "active_node": "node_1001",
        "focus_level": 0.87
    })
