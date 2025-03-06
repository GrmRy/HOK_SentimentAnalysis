import pandas as pd

def load_data(filepath='HOK-En-VADER-Analysis.csv'):
    df = pd.read_csv(filepath)
    # Convert date columns; invalid formats become NaT
    df['at'] = pd.to_datetime(df['at'], errors='coerce')
    df['repliedAt'] = pd.to_datetime(df['repliedAt'], errors='coerce')
    # Ensure text fields are strings
    df['processed_text'] = df['processed_text'].fillna('').astype(str)
    # Compute response time in hours
    df['response_hours'] = (df['repliedAt'] - df['at']).dt.total_seconds() / 3600
    return df
