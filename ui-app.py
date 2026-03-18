import streamlit as st
import pandas as pd
import joblib
from scipy.sparse import hstack

from src.preprocess import preprocess
from src.decision import decide_action

# LOAD MODELS
clf = joblib.load("models/state_model.pkl")
reg = joblib.load("models/intensity_model.pkl")
tfidf = joblib.load("models/tfidf.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title(" AI Emotion Decision System")

text = st.text_area("Enter your thoughts")

stress = st.slider("Stress Level", 0, 10, 5)
energy = st.slider("Energy Level", 0, 10, 5)
sleep = st.slider("Sleep Hours", 0, 10, 6)

time_of_day = st.selectbox(
    "Time of Day",
    ["morning", "afternoon", "evening", "night"]
)

if st.button("Analyze"):

    df = pd.DataFrame([{
        "journal_text": text,
        "stress_level": stress,
        "energy_level": energy,
        "sleep_hours": sleep,
        "time_of_day": time_of_day
    }])

    df = preprocess(df)

    X_text = tfidf.transform(df['clean_text'])
    X_meta = scaler.transform(df[['sleep_hours', 'stress_level', 'energy_level']])
    X = hstack([X_text, X_meta])

    state = clf.predict(X)[0]
    intensity = int(reg.predict(X)[0])
    confidence = max(clf.predict_proba(X)[0])

    action, when = decide_action(
        state, intensity, stress, energy, time_of_day, confidence
    )

    st.subheader(" Result")

    st.write(f"**Emotion:** {state}")
    st.write(f"**Intensity:** {intensity}")
    st.write(f"**Confidence:** {round(confidence, 2)}")
    st.write(f"**Action:** {action}")
    st.write(f"**When:** {when}")
