# src/train_model.py
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def train():
    data_path = "data/processed/processed_data.csv"
    model_path = "models/attack_model.pkl"

    print("[*] Loading processed dataset...")
    df = pd.read_csv(data_path)

    X = df.drop(['Label', 'AttackType'], axis=1)
    y = df['Label']

    print("[*] Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("[*] Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    print("[*] Evaluating model...")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, model_path)
    print(f"[+] Model saved at {model_path}")