def decide_action(state, intensity, stress, energy, time_of_day, confidence=None):

    # HANDLE UNCERTAINTY FIRST
    if confidence is not None and confidence < 0.6:
        return "pause_and_reflect", "now"

    # STRONG EMOTIONAL STATES
    if state in ["sad", "anxious"] or intensity >= 4:
        if stress > 5:
            return "box_breathing", "now"
        else:
            return "grounding", "within_15_min"

    # HIGH ENERGY POSITIVE STATES
    if state in ["happy", "focused", "calm"] and energy > 6:
        return "deep_work", "later_today"

    # LOW ENERGY
    if energy < 3:
        return "rest", "now"

    return "light_planning", "later_today"
