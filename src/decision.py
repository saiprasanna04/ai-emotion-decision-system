def decide_action(state, intensity, stress, energy, time_of_day):
    
    if stress > 7 and intensity >= 4:
        action = "box_breathing"
        
    elif state == "sad" and energy < 4:
        action = "rest"
        
    elif state == "calm" and energy > 6:
        action = "deep_work"
        
    elif state == "anxious":
        action = "grounding"
        
    elif energy < 3:
        action = "movement"
        
    else:
        action = "light_planning"
    
    
    # WHEN TO DO
    if intensity >= 4:
        when = "now"
        
    elif stress > 6:
        when = "within_15_min"
        
    elif energy > 6:
        when = "later_today"
        
    elif time_of_day == "night":
        when = "tonight"
        
    else:
        when = "tomorrow_morning"
    
    
    return action, when


def generate_message(state, action):
    return f"You seem {state}. Try {action} to feel better."
