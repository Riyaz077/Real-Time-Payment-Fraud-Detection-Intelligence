from pathlib import Path
import joblib
import pandas as pd
from .feature_engineering import build_features
from .risk_scoring import risk_score
from .explainability import reason_codes

def predict_one(payload, model_path="models/sentinelpay_model.joblib"):
    artifact = joblib.load(model_path)
    frame = build_features(pd.DataFrame([payload]))
    features = artifact["features"]
    probability = float(artifact["model"].predict_proba(frame[features])[:,1][0])
    anomaly_raw = float(artifact["isolation_forest"].decision_function(frame[features])[0])
    anomaly = 1 / (1 + max(-20, min(20, anomaly_raw*5)))
    result = risk_score(probability, anomaly)
    result.update({
        "fraud_probability": round(probability, 4),
        "anomaly_score": round(anomaly, 4),
        "reason_codes": reason_codes(frame.iloc[0].to_dict())
    })
    return result
