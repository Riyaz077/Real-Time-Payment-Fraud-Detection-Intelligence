# Methodology
1. Define a transaction schema and synthetic fraud scenarios.
2. Generate data with reproducible random seeds.
3. Perform exploratory data analysis and inspect class imbalance.
4. Split chronologically for final evaluation where timestamps permit.
5. Engineer behavioural features using only information available at decision time.
6. Train a Logistic Regression baseline and Random Forest.
7. Fit Isolation Forest on training data only.
8. Tune thresholds on validation data.
9. Evaluate once on a held-out test period.
10. Inspect false positives/negatives and reason codes.
11. Serve the model and monitor latency and input drift.

Avoid target leakage: never use post-investigation labels, chargeback outcomes or future transaction aggregates as prediction-time features.
