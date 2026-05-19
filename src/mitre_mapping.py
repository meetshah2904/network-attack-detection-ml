LABEL_TO_MITRE = {
    # --- Network Attacks ---
    "DDoS": {
        "technique": "Network Denial of Service",
        "technique_id": "T1498",
        "tactic": "Impact"
    },
    "Port Scan": {
        "technique": "Network Service Scanning",
        "technique_id": "T1046",
        "tactic": "Discovery"
    },

    # --- Credential Attacks ---
    "Brute Force": {
        "technique": "Brute Force",
        "technique_id": "T1110",
        "tactic": "Credential Access"
    },
    "Web Attack - Brute Force": {
        "technique": "Brute Force",
        "technique_id": "T1110",
        "tactic": "Credential Access"
    },

    # --- Web Attacks ---
    "Web Attack - SQL Injection": {
        "technique": "SQL Injection",
        "technique_id": "T1190",
        "tactic": "Initial Access"
    },
    "Web Attack - XSS": {
        "technique": "Cross-Site Scripting",
        "technique_id": "T1059.007",
        "tactic": "Execution"
    },

    # --- Infiltration ---
    "Infiltration": {
        "technique": "Ingress Tool Transfer",
        "technique_id": "T1105",
        "tactic": "Command and Control"
    },

    # --- Botnet ---
    "Botnet": {
        "technique": "Application Layer Protocol",
        "technique_id": "T1071",
        "tactic": "Command and Control"
    },

    # --- Benign traffic ---
    "BENIGN": {
        "technique": "None",
        "technique_id": "None",
        "tactic": "None"
    }
}