import numpy as np
import pandas as pd
from datetime import datetime, timedelta, timezone

def generate_transactions(n=5000, fraud_rate=0.025, seed=42):
    rng = np.random.default_rng(seed)
    fraud = rng.random(n) < fraud_rate
    amounts = rng.lognormal(mean=5.0, sigma=1.0, size=n)
    amounts[fraud] *= rng.uniform(2.0, 8.0, fraud.sum())
    avg = rng.lognormal(mean=5.0, sigma=0.65, size=n)
    device_new = rng.binomial(1, np.where(fraud, 0.48, 0.07))
    beneficiary_new = rng.binomial(1, np.where(fraud, 0.62, 0.12))
    velocity = rng.poisson(np.where(fraud, 5.0, 1.2))
    distance = rng.gamma(shape=1.5, scale=np.where(fraud, 35.0, 5.0))
    failed = rng.poisson(np.where(fraud, 1.8, 0.15))
    now = datetime.now(timezone.utc)
    times = [now - timedelta(seconds=int(x)) for x in rng.integers(0, 30*86400, n)]
    df = pd.DataFrame({
        "transaction_id": [f"SP{idx:09d}" for idx in range(n)],
        "timestamp": times,
        "amount": amounts.round(2),
        "sender_id": [f"S{v:06d}" for v in rng.integers(1, max(2,n//4), n)],
        "receiver_id": [f"R{v:06d}" for v in rng.integers(1, max(2,n//3), n)],
        "transaction_type": rng.choice(["P2P","MERCHANT","BILL"], n, p=[.62,.28,.10]),
        "device_new": device_new,
        "beneficiary_new": beneficiary_new,
        "transactions_last_10m": velocity,
        "avg_amount_30d": avg.round(2),
        "geo_distance_km": distance.round(2),
        "failed_attempts_1h": failed,
        "is_fraud": fraud.astype(int)
    })
    return df
