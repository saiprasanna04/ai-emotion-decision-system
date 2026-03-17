#  Error Analysis

We analyzed failure cases to understand model limitations in real-world noisy scenarios.

---

## Case 1: Very Short Input
Text: "ok" 
Prediction: neutral 
Issue:
- Text contains almost no emotional signal

Why model failed:
- TF-IDF relies on meaningful words
- No metadata strong enough to compensate

Fix:
- Mark as uncertain
- Trigger fallback logic

---

## Case 2: Conflicting Signals
Text: "I feel great"
Stress: 9 
Prediction: happy 

Issue:
- Text and metadata contradict each other

Why model failed:
- Model trusts text more than metadata

Fix:
- Add conflict detection
- Increase weight for stress in decision layer

---

## Case 3: Ambiguous Text
Text: "today was different" 
Prediction: neutral 

Issue:
- Emotion unclear

Why model failed:
- Lack of emotional keywords

Fix:
- Use context features (previous mood, energy)

---

## Case 4: Noisy Label
Text: "I’m calm and relaxed"
True label: sad 

Issue:
- Incorrect ground truth label

Why model failed:
- Model learns wrong mapping

Fix:
- Label cleaning or filtering

---

## Case 5: Mixed Emotions
Text: "I’m tired but excited" 
Prediction: happy 

Issue:
- Multiple emotions present

Why model failed:
- Model predicts dominant emotion only

Fix:
- Multi-label or weighted emotion scoring

---

## Case 6: High Intensity Misclassification
Text: "I’m slightly annoyed"
Predicted intensity: 4 

Issue:
- Overestimation of intensity

Why model failed:
- Keyword “annoyed” strongly weighted

Fix:
- Use modifiers (slightly, very) in preprocessing

---

## Case 7: Missing Metadata
Text: "feeling low"
Stress: missing 

Issue:
- Missing context reduces accuracy

Fix:
- Fill missing values with defaults or averages

---

## Case 8: Over-reliance on Text
Text: "I’m fine"
Stress: 8 

Prediction: neutral 

Issue:
- Model ignores stress signal

Fix:
- Combine features more effectively

---

## Case 9: Time Context Ignored
Text: "can’t sleep"
Time: morning 

Issue:
- Time contradicts input

Fix:
- Add time-aware logic

---

## Case 10: Very Noisy Input
Text: "idk just meh idk"
Prediction: neutral 

Issue:
- Unstructured and unclear language

Fix:
- Detect low-quality input → mark uncertain
