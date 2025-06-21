# Cross-Device Sync Protocol (CDSP)

## Purpose
Establish a lightweight, extensible standard for synchronizing symbolic state, neural input, and node focus across multiple Fractality-compatible devices.

---

## Core Payload Format

```json
{
  "timestamp": "2025-06-21T18:30:00Z",
  "user_id": "grazi",
  "active_node": "node_1001",
  "focus_level": 0.87,
  "current_mode": "dream",
  "glyph_state": {
    "id": "glyph_abc",
    "status": "fading"
  }
}
```

---

## Sync Modes

| Mode         | Description                              |
|--------------|------------------------------------------|
| Push         | Source device sends state update         |
| Pull         | Receiver requests current session state  |
| Hybrid       | Devices negotiate sync in real time      |

---

## Security Considerations

- Auth via per-device keys or token handshake
- All sync packets signed + timestamped
- Optional local-only mode for private states

---

## Future Features

- Shared glyph resonance (collaborative states)
- Inter-device haptics (trigger pulse from desktop → wristband)
- Symbolic beacon broadcasts to nearby nodes
