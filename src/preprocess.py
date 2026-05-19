# src/preprocess.py
import pandas as pd
import os
import numpy as np

def preprocess():
    input_path = "data/raw/sample.csv"
    output_path = "data/processed/processed_data.csv"

    print("[*] Loading dataset...")
    df = pd.read_csv(input_path)

    df.columns = df.columns.str.strip()

    if 'Label' not in df.columns:
        raise Exception("Dataset must contain a Label column")

    # Preserve original attack type
    df['AttackType'] = df['Label']

    # Binary label for ML
    df['Label'] = df['Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)

    # Keep numeric + AttackType
    df = df.select_dtypes(include=[np.number]).join(df['AttackType'])

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"[+] Preprocessing completed. Saved to {output_path}")