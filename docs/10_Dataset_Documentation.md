# Dataset Documentation
The included CSV is generated locally and is fully synthetic. It contains no real UPI identifiers or customer records.

| Field | Meaning |
|---|---|
| transaction_id | Synthetic event identifier |
| timestamp | Event timestamp |
| amount | Amount in INR |
| sender_id / receiver_id | Random synthetic entity tokens |
| transaction_type | P2P, merchant or bill payment |
| device_new | Whether the device is new to the synthetic sender |
| beneficiary_new | Whether receiver is new to sender |
| transactions_last_10m | Synthetic recent transaction count |
| avg_amount_30d | Synthetic historical mean amount |
| geo_distance_km | Simulated distance from prior activity |
| failed_attempts_1h | Simulated recent failed attempts |
| is_fraud | Synthetic ground-truth label |

Synthetic labels are generated from programmed scenarios and do not represent real-world fraud prevalence or ground truth. Use a public dataset such as PaySim for an additional benchmark, after checking its license and documenting its non-UPI nature.
