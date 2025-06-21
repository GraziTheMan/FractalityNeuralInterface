# glyph_generator.py
# Creates symbolic glyph objects based on neural resonance patterns

import hashlib

def generate_glyph(signal, intensity):
    base = f"{signal}-{intensity}"
    hex_digest = hashlib.sha256(base.encode()).hexdigest()[:8]
    glyph = {
        "id": f"glyph_{hex_digest}",
        "signal": signal,
        "intensity": intensity,
        "symbolic_code": hex_digest,
        "style": {
            "shape": "spiral" if signal == "theta_surge" else "starburst",
            "color": "#ccf" if intensity < 0.6 else "#f8f"
        }
    }
    return glyph

if __name__ == "__main__":
    from pprint import pprint
    pprint(generate_glyph("gamma_sync", 0.92))
