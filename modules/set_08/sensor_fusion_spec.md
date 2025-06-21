# Sensor Fusion Mapping Spec (Fractality Environment Integration)

## Sensors & Inputs

| Type         | Measurement           | Output Range        | Mapped Symbolic State         |
|--------------|------------------------|----------------------|-------------------------------|
| Ambient Light| Lux                    | 0–1000+              | dim_cave / twilight / daylight |
| Sound        | Decibel Level (dB)     | 0–120+               | silence / conversation / chaotic |
| Camera       | Image context (tags)   | Strings              | organic / human / abstract / mythic |
| Optional     | Infrared / Thermal     | Temperature gradients| spectral / dreamwarm / nightcold |

---

## Symbol Integration

Mapped environmental states are tagged onto:
- Active nodes
- Trails (e.g., “formed during twilight”)
- Glyphs (e.g., “encoded under chaotic audio”)
- Session metadata

---

## Feedback Triggers

| Input Change       | Response                                |
|--------------------|-----------------------------------------|
| Light drops sharply| UI contrast shifts, nodes glow softly   |
| Sudden sound burst | Trail snap or ripple effect             |
| Face in frame      | “Presence Detected” node or glyph       |
| Organic pattern    | Create nature-linked node with trail    |

---

## Future Expansion

- Emotion inference via facial tone + ambient overlay
- Pattern recognition layers for mythic activation
- Shared environmental beacon system (resonant room states)
