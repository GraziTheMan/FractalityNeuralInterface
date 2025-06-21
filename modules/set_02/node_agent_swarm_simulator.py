# node_agent_swarm_simulator.py
# Simulates multiple specialized node agents processing events in parallel

import random
import time

AGENTS = {
    "FocusNode": ["beta_burst", "alpha_peak"],
    "DreamNode": ["theta_surge", "REM_spike"],
    "SyncNode": ["gamma_sync", "p300_response"],
    "EmotionNode": ["hrv_coherence", "eda_spike"]
}

def simulate_event():
    agent = random.choice(list(AGENTS.keys()))
    signal = random.choice(AGENTS[agent])
    print(f"[{agent}] received signal: {signal}")
    process_event(agent, signal)

def process_event(agent, signal):
    if agent == "FocusNode":
        print(" -> Emphasizing focused node cluster")
    elif agent == "DreamNode":
        print(" -> Generating symbolic dream trail")
    elif agent == "SyncNode":
        print(" -> Initiating idea convergence")
    elif agent == "EmotionNode":
        print(" -> Modulating UI feedback (color, animation)")
    print()

if __name__ == "__main__":
    print("Simulating Swarm Node Agents...
")
    for _ in range(5):
        simulate_event()
        time.sleep(1)
