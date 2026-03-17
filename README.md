# AI Emotion Understanding & Decision System

## Approach
We built a hybrid system combining:
- ML models for emotion understanding
- Rule-based logic for decision making

## Models
- Emotion: Logistic Regression (TF-IDF + metadata)
- Intensity: Random Forest Regression

## Features
- Text (TF-IDF)
- Metadata (sleep, stress, energy)

## Decision Engine
Uses predicted emotion, intensity, and context to:
- Suggest actions
- Recommend timing

## Uncertainty
- Based on prediction probability
- Flagged when confidence < 0.6

## How to Run
pip install -r requirements.txt
python src/train.py
python src/predict.py
