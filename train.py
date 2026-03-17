import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib

from preprocess import load_data, preprocess

df = load_data("data/train.csv")
df = preprocess(df)

# TEXT FEATURES
tfidf = TfidfVectorizer(max_features=3000)
X_text = tfidf.fit_transform(df['clean_text'])

# METADATA
meta_cols = ['sleep_hours', 'stress_level', 'energy_level']
scaler = StandardScaler()
X_meta = scaler.fit_transform(df[meta_cols])

# COMBINE
from scipy.sparse import hstack
X = hstack([X_text, X_meta])

# TARGETS
y_state = df['emotional_state']
y_intensity = df['intensity']

# MODELS
clf = LogisticRegression(max_iter=200)
clf.fit(X, y_state)

reg = RandomForestRegressor()
reg.fit(X.toarray(), y_intensity)

# SAVE
joblib.dump(clf, "models/state_model.pkl")
joblib.dump(reg, "models/intensity_model.pkl")
joblib.dump(tfidf, "models/tfidf.pkl")
joblib.dump(scaler, "models/scaler.pkl")
