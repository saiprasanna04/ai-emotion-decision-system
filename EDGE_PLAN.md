\#  Edge Deployment Plan

## Goal
Deploy the system on mobile / on-device for real-time emotional assistance.

---

## Model Choice
- Logistic Regression (lightweight)
- Random Forest (moderate size)

Reason:
- Fast inference
- Low memory usage

---

## Deployment Strategy
- Convert models using ONNX or TensorFlow Lite
- Run inference locally on device
- No need for internet connection

---

## Latency
- Prediction time < 100 ms
- Suitable for real-time interaction

---

## Trade-offs

| Factor | Trade-off |
|------|----------|
| Accuracy | Slightly lower than deep models |
| Speed | Very fast |
| Memory | Low |

---

## Optimization Techniques
- Reduce feature size (limit TF-IDF vocab)
- Use model compression
- Quantization for mobile deployment

---

## Robustness on Edge
- Handle missing data locally
- Detect uncertain inputs
- Use fallback rules

---

## Final Insight

A lightweight hybrid system is ideal for real-world deployment where speed, privacy, and reliability are critical.
