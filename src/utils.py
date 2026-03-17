import numpy as np

# -------------------------------
# Confidence & Uncertainty
# -------------------------------

def get_confidence(probs):
    """
    Returns the maximum probability from model output
    """
    return float(np.max(probs))


def get_uncertainty_flag(confidence, threshold=0.6):
    """
    Basic uncertainty based on confidence threshold
    """
    return 1 if confidence < threshold else 0


# -------------------------------
# Text Handling
# -------------------------------

def is_text_short(text):
    """
    Checks if text is too short (low information)
    """
    if text is None:
        return True
    return len(str(text).strip().split()) <= 2


# -------------------------------
# Missing Values Handling
# -------------------------------

def handle_missing_values(df):
    """
    Fill missing values with reasonable defaults
    """
    df.fillna({
        'sleep_hours': df['sleep_hours'].mean(),
        'stress_level': df['stress_level'].mean(),
        'energy_level': df['energy_level'].mean(),
        'previous_day_mood': 'neutral',
        'journal_text': ''
    }, inplace=True)
    
    return df


# -------------------------------
# Intensity Normalization
# -------------------------------

def normalize_intensity(value):
    """
    Ensure intensity is always between 1 and 5
    """
    try:
        value = int(round(value))
    except:
        value = 3  # fallback

    return max(1, min(5, value))


# -------------------------------
# Conflict Detection
# -------------------------------

def has_conflict(text, stress_level):
    """
    Detects mismatch between text sentiment and stress signal
    """
    if text is None:
        return False

    text = str(text).lower()

    positive_words = ["good", "fine", "happy", "okay", "ok"]
    
    if any(word in text for word in positive_words) and stress_level is not None:
        if stress_level > 7:
            return True

    return False


# -------------------------------
# Advanced Uncertainty Logic
# -------------------------------

def compute_uncertainty(text, confidence, stress_level):
    """
    Combines multiple signals to detect uncertainty
    """
    # Low model confidence
    if confidence < 0.6:
        return 1

    # Very short text
    if is_text_short(text):
        return 1

    # Conflicting signals
    if has_conflict(text, stress_level):
        return 1

    return 0
