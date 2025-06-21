# HUD Overlay Spec (Fractality NeuroUI)

## Purpose
Define an optional, dynamic overlay interface that visualizes neural state interpretations in real-time during Fractality sessions.

---

## Features

- Floating neural signal indicators (alpha, beta, gamma)
- Live display of most recent pattern + action taken
- HUD glyphs for active swarm agents
- Consent/status beacon (color coded by mode)

---

## Regions

| HUD Zone     | Purpose                        |
|--------------|--------------------------------|
| Top Left     | Current signal + intensity     |
| Bottom Right | Recent node interactions       |
| Top Right    | Active agent icons (swarm)     |
| Center Fade  | Pulse feedback (glow/shimmer)  |

---

## Example Glyphs

- 🧠 Alpha → calm resonance
- ⚡ Beta → spike of creation
- 🌌 Theta → dream activation
- 🔗 P300 → node link trigger
- 💫 Gamma → convergence

---

## Styles

- Subtle animations (pulse, ripple)
- Fades out during inactivity
- Transparent background for UI blending

---

## Integration Path

- Add to Fractality UI via WebGL or Canvas layer
- Pulls from neural event stream via WebSocket
- Emits feedback events based on interaction

