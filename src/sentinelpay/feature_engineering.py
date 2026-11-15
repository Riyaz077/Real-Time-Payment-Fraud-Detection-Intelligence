import pandas as pd
from .preprocessing import validate_transactions

FEATURES = ["amount","amount_to_avg_ratio","device_new","beneficiary_new",
            "transactions_last_10m","geo_distance_km","failed_attempts_1h"]

def build_features(df):
    x = validate_transactions(df)
    x["amount_to_avg_ratio"] = (x["amount"] / x["avg_amount_30d"]).clip(0, 100)
    return x
