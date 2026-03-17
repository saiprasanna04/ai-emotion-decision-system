import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_text(text):
    return str(text).lower()

def preprocess(df):
    df['clean_text'] = df['journal_text'].apply(clean_text)
    
    # Fill missing values
    df.fillna({
        'sleep_hours': df['sleep_hours'].mean(),
        'stress_level': df['stress_level'].mean(),
        'energy_level': df['energy_level'].mean(),
        'previous_day_mood': 'neutral'
    }, inplace=True)
    
    return df
