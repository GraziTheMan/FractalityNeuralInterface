# dream_node_generator.py
# Translates symbolic dream signals into Fractality node creation commands

def dream_to_node(pattern):
    dream_map = {
        "REM_spike": {"symbol": "Dream Guardian", "tag": "mythic"},
        "theta_drift": {"symbol": "Ancestral Memory", "tag": "deep"},
        "breath_shift": {"symbol": "Elemental Motif", "tag": "elemental"}
    }
    if pattern in dream_map:
        node = {
            "action_type": "generate_node",
            "label": dream_map[pattern]["symbol"],
            "tags": [dream_map[pattern]["tag"]],
            "style": {
                "color": "#aaf",
                "glow": True
            }
        }
        return node
    return None

if __name__ == "__main__":
    from pprint import pprint
    pprint(dream_to_node("theta_drift"))
