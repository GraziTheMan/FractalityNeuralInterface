# resonance_packet_broadcaster.py
# Broadcasts symbolic resonance states to other users or agents over WebSockets

import json
import asyncio
import websockets

RES_PACKET = {
    "user_id": "grazi",
    "resonance_state": {
        "focus": 0.92,
        "emotion": "curious",
        "active_node": "node_456",
        "glyph": "glyph_abc123",
        "intensity": 0.88
    },
    "timestamp": "2025-06-21T20:40:00Z"
}

async def broadcast_resonance():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(RES_PACKET))
        print(f"📡 Sent resonance packet: {RES_PACKET['resonance_state']}")

if __name__ == "__main__":
    asyncio.run(broadcast_resonance())
