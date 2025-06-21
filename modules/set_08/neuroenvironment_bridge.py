# neuroenvironment_bridge.py
# Captures and maps ambient light, sound, and image input into symbolic Fractality state changes

def process_environment(light_lux, sound_db, image_context):
    symbolic_state = {}

    # Light mapping
    if light_lux < 100:
        symbolic_state["lighting"] = "dim_cave"
    elif light_lux < 500:
        symbolic_state["lighting"] = "twilight"
    else:
        symbolic_state["lighting"] = "daylight"

    # Sound mapping
    if sound_db < 30:
        symbolic_state["audio"] = "silence"
    elif sound_db < 65:
        symbolic_state["audio"] = "conversation"
    else:
        symbolic_state["audio"] = "chaotic"

    # Image context (stub)
    if "plant" in image_context:
        symbolic_state["visual"] = "organic"
    elif "face" in image_context:
        symbolic_state["visual"] = "human"
    else:
        symbolic_state["visual"] = "abstract"

    print("🌐 Environment mapped to symbolic state:")
    for k, v in symbolic_state.items():
        print(f"  {k}: {v}")
    return symbolic_state

# Example usage
if __name__ == "__main__":
    process_environment(light_lux=85, sound_db=50, image_context=["plant", "green"])
