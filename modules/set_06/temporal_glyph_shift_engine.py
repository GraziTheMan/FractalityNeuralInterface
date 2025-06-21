# temporal_glyph_shift_engine.py
# Modulates symbolic glyphs as patterns evolve over time

def evolve_glyph_state(glyph, duration_seconds):
    if duration_seconds > 60:
        glyph["style"]["fade"] = True
        glyph["style"]["pulse"] = "slow"
        glyph["tags"] = list(set(glyph.get("tags", []) + ["legacy"]))
        print(f"🌀 Glyph faded into legacy state: {glyph['id']}")
    else:
        print(f"Glyph remains active: {glyph['id']}")
    return glyph

# Example
if __name__ == "__main__":
    glyph = {
        "id": "glyph_abc123",
        "style": {},
        "tags": ["insight"]
    }
    evolve_glyph_state(glyph, duration_seconds=120)
