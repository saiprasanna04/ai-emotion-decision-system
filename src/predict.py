import pandas as pd
import joblib
from scipy.sparse import hstack

from preprocess import load_data, preprocess
from decision import decide_action, generate_message

# LOAD
df = load_data("data/test.csv")
df = preprocess(df)

clf = joblib.load("models/state_model.pkl")
reg = joblib.load("models/intensity_model.pkl")
tfidf = joblib.load("models/tfidf.pkl")
scaler = joblib.load("models/scaler.pkl")

# FEATURES
X_text = tfidf.transform(df['clean_text'])
meta_cols = ['sleep_hours', 'stress_level', 'energy_level']
X_meta = scaler.transform(df[meta_cols])

X = hstack([X_text, X_meta])

# PREDICT
state_probs = clf.predict_proba(X)
states = clf.predict(X)
intensity = reg.predict(X)

results = []

for i in range(len(df)):
    conf = max(state_probs[i])
    uncertain = 1 if conf < 0.6 else 0
    
    action, when = decide_action(
        states[i],
        int(intensity[i]),
        df.iloc[i]['stress_level'],
        df.iloc[i]['energy_level'],
        df.iloc[i]['time_of_day']
    )
    
    msg = generate_message(states[i], action)
    
    results.append({
        "id": df.iloc[i]['id'],
        "predicted_state": states[i],
        "predicted_intensity": int(intensity[i]),
        "confidence": conf,
        "uncertain_flag": uncertain,
        "what_to_do": action,
        "when_to_do": when
    })

out = pd.DataFrame(results)
out.to_csv("outputs/predictions.csv", index=False)
