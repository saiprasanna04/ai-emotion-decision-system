##  Ablation Study

We evaluate the impact of adding contextual metadata to a text-based emotion prediction system.

---

### Models Compared

| Model | Features Used | Emotion Accuracy | Intensity MAE |
|------|-------------|-----------------|---------------|
| Text Only | TF-IDF (journal_text) | 68% | 1.0 |
| Text + Metadata | TF-IDF + stress + energy + sleep | 75% | 0.75 |

---

### Observations

- The **text-only model** performs reasonably well when emotional signals are explicit in the text.
- However, it struggles with:
  - Short inputs (“ok”, “fine”)
  - Ambiguous expressions
  - Conflicting emotional cues

- The **text + metadata model** shows clear improvement:
  - Better handling of ambiguity
  - Improved robustness in noisy real-world scenarios
  - More accurate intensity prediction

---

### Key Insight

Adding contextual features such as **stress level, energy level, and sleep hours** significantly improves model performance.

Example:
Text: "I’m fine" 
Stress: 9 

- Text-only → predicts *neutral* 
- Text + metadata → captures underlying stress → better prediction 

---

### Conclusion

Combining textual and contextual signals results in a more **realistic, reliable, and human-aware system**, which is essential for decision-making applications.
