import pandas as pd
from src.sentinelpay.feature_engineering import build_features
def test_amount_ratio():
    df=pd.DataFrame([{"amount":200,"avg_amount_30d":100,"device_new":1,
    "beneficiary_new":0,"transactions_last_10m":2,"geo_distance_km":1,
    "failed_attempts_1h":0}])
    out=build_features(df)
    assert out.iloc[0]["amount_to_avg_ratio"] == 2
