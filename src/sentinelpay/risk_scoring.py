def risk_score(fraud_probability, anomaly_score=0.0):
    # anomaly_score expected in [0, 1]; illustrative weights only
    p = min(max(float(fraud_probability), 0), 1)
    a = min(max(float(anomaly_score), 0), 1)
    score = round(100 * (0.8*p + 0.2*a))
    band = "CRITICAL" if score >= 85 else "HIGH" if score >= 65 else "MEDIUM" if score >= 40 else "LOW"
    return {"risk_score": score, "risk_band": band}
