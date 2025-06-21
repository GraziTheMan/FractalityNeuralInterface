# feedback_actuator.py
# Triggers visual, audio, or haptic feedback in response to neural events

def trigger_feedback(event):
    signal = event.get("signal")
    intensity = event.get("intensity", 0.5)

    if signal == "alpha_peak":
        return visual_feedback("soft_glow", intensity)
    elif signal == "beta_burst":
        return audio_feedback("chime_rise", intensity)
    elif signal == "theta_surge":
        return visual_feedback("dream_trail", intensity)
    elif signal == "p300_response":
        return audio_feedback("ping_link", intensity)
    elif signal == "gamma_sync":
        return haptic_feedback("pulse", intensity)
    else:
        print("Unknown signal. No feedback triggered.")

def visual_feedback(effect, intensity):
    print(f"[Visual] Triggering {effect} at intensity {intensity}")

def audio_feedback(effect, intensity):
    print(f"[Audio] Playing {effect} at intensity {intensity}")

def haptic_feedback(effect, intensity):
    print(f"[Haptic] Vibrating {effect} at intensity {intensity}")

# Example usage
if __name__ == "__main__":
    mock_event = {
        "signal": "theta_surge",
        "intensity": 0.8
    }
    trigger_feedback(mock_event)
