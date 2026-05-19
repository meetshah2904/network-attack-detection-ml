import pandas as pd
import joblib
import json
import os
from datetime import datetime
from mitre_mapping import LABEL_TO_MITRE

def normalize_label(label):
    val = str(label).strip()
    if val == "0":
        return "BENIGN"
    if val == "1":
        return "Web Attack - Brute Force"
    if val == "2":
        return "Web Attack - SQL Injection"
    if val == "3":
        return "Web Attack - XSS"

    for bad_dash in ["–", "—", "−", "\u0096", "\u2013", "\u2014"]:
        val = val.replace(bad_dash, "-")
    return val
def correlate_attacks():
    print("[*] Loading model and dataset...")
    model = joblib.load("models/attack_model.pkl")
    df = pd.read_csv("data/processed/processed_data.csv")

    # Drop non-numeric columns for prediction
    X = df.drop(['Label', 'AttackType'], axis=1)
    predictions = model.predict(X)

    correlated_events = []
    unmapped_labels = set()

    for i, pred in enumerate(predictions[:200]):
        if pred == 1:
            raw_label = df.iloc[i]['AttackType']
            attack_type = normalize_label(raw_label)

            # Skip benign traffic
            if attack_type == "BENIGN":
                continue

            mitre = LABEL_TO_MITRE.get(
                attack_type,
                {"technique": "Unknown", "technique_id": "Unknown", "tactic": "Unknown"}
            )
            if mitre["technique"] == "Unknown":
                unmapped_labels.add(attack_type)
            event = {
                "timestamp": datetime.now().isoformat(),
                "attack_type": attack_type,
                "prediction": "Malicious",
                "mitre_tactic": mitre["tactic"],
                "mitre_technique_id": mitre["technique_id"],
                "mitre_technique": mitre["technique"],
                "confidence": "High"
            }
            correlated_events.append(event)

    # Save results
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/mitre_attack_report.json", "w") as f:
        json.dump(correlated_events, f, indent=4)

    if unmapped_labels:
        with open("outputs/unmapped_labels.txt", "w") as f:
            for lbl in sorted(unmapped_labels):
                f.write(lbl + "\n")

    print("[+] MITRE ATT&CK correlation completed. Report saved to outputs/mitre_attack_report.json")
    if unmapped_labels:
        print(f"Unmapped labels found. See outputs/unmapped_labels.txt for details.")