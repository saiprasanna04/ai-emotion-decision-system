#  AI Emotion Understanding & Decision System

##  Problem Statement
Build a system that understands human emotional state from noisy, real-world inputs and guides users toward better actions.

This system goes beyond prediction:
**Understand → Decide → Guide**

---

##  System Flow

1. User input (journal + metadata)
2. Emotion prediction (ML model)
3. Intensity prediction (regression)
4. Decision engine (rule-based reasoning)
5. Uncertainty estimation
6. Final output (action + timing)

---

##  Approach

 **hybrid system**:

- ML models → predict emotional state & intensity  
- Rule-based logic → decide *what to do* and *when*

### Core Logic Examples:
- High stress + high intensity → immediate intervention
- High energy + calm → deep work
- Low energy → rest

---

##  Models Used

- Logistic Regression → Emotion classification  
- Random Forest → Intensity regression  

### Why Regression for Intensity?
Intensity is modeled as regression to capture subtle variations, then mapped to a 1–5 scale.

---

##  Feature Importance

- **Text (TF-IDF)** → primary emotional signal  
- **Metadata (stress, energy, sleep)** → resolves ambiguity  

Example:
> “I’m fine” + stress = 9 → likely not actually fine

---

##  Ablation Study:

### Models Compared

| Model | Features Used | Emotion Accuracy | Intensity MAE |
|------|-------------|-----------------|---------------|
| Text Only | TF-IDF (journal_text) | 68% | 1.0 |
| Text + Metadata | TF-IDF + stress + energy + sleep | 75% | 0.75 |


 Metadata significantly improves performance in noisy and conflicting cases.

---

##  Uncertainty Modeling

We estimate uncertainty using:

- Prediction confidence  
- Short text detection (“ok”, “fine”)  
- Conflict detection (text vs metadata mismatch)

### Rule:
- confidence < 0.6 → uncertain_flag = 1

---

##  Decision Engine

Uses:
- predicted emotion  
- intensity  
- stress level  
- energy level  
- time of day  

### Example Decisions:
- High stress → breathing / grounding  
- Low energy → rest  
- Calm + high energy → deep work  

---

##  Robustness

Handles real-world issues:

- Short text → marked uncertain  
- Missing values → filled with defaults  
- Conflicting signals → resolved via rules  

---

##  Sample Output

| Input | State | Intensity | Action | When |
|------|------|----------|--------|------|
| "I feel very tired" | sad | 4 | rest | now |
| "Feeling motivated" | happy | 2 | deep_work | later_today |

---

##  Features Used

- Text → TF-IDF  
- Metadata → sleep, stress, energy, time_of_day  

---

##  How to Run

```bash
pip install -r requirements.txt
python src/train.py
python src/predict.py

##  UI Demo

Run:
streamlit run ui_app.py

This launches a simple interactive interface to test the system.
