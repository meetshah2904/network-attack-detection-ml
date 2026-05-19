# src/main.py
from sample_creator import create_sample
from preprocess import preprocess
from train_model import train
from xai_explainer import explain
from correlation_engine import correlate_attacks

def run_full_pipeline():
    print("[*] Step 1: Creating sample dataset...")
    input_file = input("Enter path to dataset (CSV or PCAP): ").strip()
    create_sample(input_file)

    print("[*] Step 2: Preprocessing dataset...")
    preprocess()

    print("[*] Step 3: Training ML model...")
    train()

    print("[*] Step 4: Explainable AI (SHAP)...")
    explain()

    print("[*] Step 5: MITRE ATT&CK correlation...")
    correlate_attacks()
    print("[+] Full pipeline completed successfully!")
if __name__ == "__main__":
    run_full_pipeline()