# AI Emotion Understanding & Decision System

##  Problem Statement
To build a system that understands human emotional state and guides actions under noisy and imperfect signals.

##  Approach
We use a hybrid system:
- ML models → emotion + intensity
- Rule-based logic → decision making

##  Models Used
- Logistic Regression (emotion classification)
- Random Forest (intensity regression)

##  Why Regression for Intensity?
Intensity is treated as regression to capture subtle variations and then mapped to 1–5.

##  Feature Importance
- Text (TF-IDF) → primary signal
- Metadata → resolves ambiguity

Example:
“I’m fine” + high stress → not actually fine

##  Ablation Study
- Text-only model → weaker on ambiguous inputs
- Text + metadata → improved robustness

##  Uncertainty Modeling
combine:
- Model confidence
- Short text detection
- Conflict detection

## Uncertainty
- Based on prediction probability
- Flagged when confidence < 0.6

##  Decision Logic
Uses:
- emotion
- intensity
- stress
- energy
- time of day

## Decision Engine
Uses predicted emotion, intensity, and context to:
- Suggest actions
- Recommend timing

##  Robustness
- Short text → uncertain
- Missing values → filled
- Conflicts → detected

## Features
- Text (TF-IDF)
- Metadata (sleep, stress, energy)

## How to Run
pip install -r requirements.txt
python src/train.py
python src/predict.py
