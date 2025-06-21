# multi_agent_choreographer.py
# Coordinates behavior among symbolic node agents using orchestration rules

AGENTS = {
    "FocusNode": {"active": False},
    "DreamNode": {"active": False},
    "SyncNode": {"active": False}
}

def activate_agent(name):
    AGENTS[name]["active"] = True
    print(f"[{name}] is now ACTIVE.")

def deactivate_agent(name):
    AGENTS[name]["active"] = False
    print(f"[{name}] is now INACTIVE.")

def orchestrate(event_type):
    if event_type == "creative_burst":
        activate_agent("FocusNode")
        activate_agent("DreamNode")
    elif event_type == "integration_moment":
        activate_agent("SyncNode")
        deactivate_agent("DreamNode")

# Example flow
if __name__ == "__main__":
    orchestrate("creative_burst")
    orchestrate("integration_moment")
