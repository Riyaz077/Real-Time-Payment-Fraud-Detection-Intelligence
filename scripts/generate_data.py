import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.sentinelpay.data_generator import generate_transactions
p=argparse.ArgumentParser()
p.add_argument("--rows", type=int, default=5000)
p.add_argument("--fraud-rate", type=float, default=.025)
p.add_argument("--output", default="data/sample/sample_transactions.csv")
a=p.parse_args()
Path(a.output).parent.mkdir(parents=True, exist_ok=True)
generate_transactions(a.rows, a.fraud_rate).to_csv(a.output, index=False)
print(f"Wrote {a.rows} synthetic rows to {a.output}")
