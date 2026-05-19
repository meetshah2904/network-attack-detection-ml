# src/sample_creator.py
import pandas as pd
import os

def create_sample(input_file):
    print(f"[*] Loading dataset from {input_file}...")
    if input_file.endswith(".csv"):
        try:
            df = pd.read_csv(input_file, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(input_file, encoding="ISO-8859-1")
    elif input_file.endswith(".pcap"):
        import pyshark
        print("[*] Parsing PCAP with PyShark...")
        cap = pyshark.FileCapture(input_file, only_summaries=True)
        rows = []
        for pkt in cap:
            rows.append({
                "No": pkt.no,
                "Time": pkt.time,
                "Source": pkt.source,
                "Destination": pkt.destination,
                "Protocol": pkt.protocol,
                "Length": pkt.length,
                "Info": pkt.info,
                "Label": "BENIGN"
            })
        df = pd.DataFrame(rows)
        cap.close()
    else:
        raise ValueError("Unsupported file format. Use .csv or .pcap")

    sample = df.sample(n=min(5000, len(df)), random_state=42)
    os.makedirs("data/raw", exist_ok=True)
    output_path = "data/raw/sample.csv"
    sample.to_csv(output_path, index=False)
    print(f"[+] Sample dataset saved to {output_path}")