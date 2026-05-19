# src/xai_explainer.py
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

def explain():
    print("[*] Loading model and data...")
    model = joblib.load("models/attack_model.pkl")
    df = pd.read_csv("data/processed/processed_data.csv")

    X = df.drop(['Label', 'AttackType'], axis=1)
    X_sample = X.sample(200, random_state=42)

    print("[*] Initializing SHAP Explainer...")
    explainer = shap.TreeExplainer(model)

    print("[*] Generating SHAP values...")
    shap_values = explainer.shap_values(X_sample)

    shap.summary_plot(shap_values[1], X_sample, show=False)
    plt.savefig("xai_feature_importance.png", dpi=300)
    plt.show()

    shap.summary_plot(shap_values[1], X_sample, plot_type="bar", show=False)
    plt.savefig("xai_feature_importance_bar.png", dpi=300)
    plt.show()

    print("[+] SHAP explanation completed")