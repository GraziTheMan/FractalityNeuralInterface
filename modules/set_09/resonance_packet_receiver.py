# resonance_packet_receiver.py
# Listens for symbolic resonance packets from other users

import asyncio
import websockets

async def receive_resonance():
    async def handler(websocket, path):
        async for message in websocket:
            print(f"📥 Received packet: {message}")

    print("🌀 Listening for resonance on ws://localhost:8765...")
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(receive_resonance())
