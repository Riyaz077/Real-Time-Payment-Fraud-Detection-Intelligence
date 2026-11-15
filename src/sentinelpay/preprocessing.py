import pandas as pd

REQUIRED = ["amount","device_new","beneficiary_new","transactions_last_10m",
            "avg_amount_30d","geo_distance_km","failed_attempts_1h"]

def validate_transactions(df):
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    out = df.copy()
    for c in REQUIRED:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    out[REQUIRED] = out[REQUIRED].fillna(0)
    out["amount"] = out["amount"].clip(lower=0)
    out["avg_amount_30d"] = out["avg_amount_30d"].clip(lower=1)
    return out
