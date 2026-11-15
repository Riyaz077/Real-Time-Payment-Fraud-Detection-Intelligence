# Model Evaluation
Report:
- Confusion matrix
- Precision, recall and F1-score
- ROC-AUC and especially PR-AUC
- False-positive rate and false-negative rate
- Recall at a fixed alert volume / precision@k
- Calibration curve and Brier score
- Inference latency (p50/p95) and throughput

Because fraud is rare, accuracy can be misleading. Select operating thresholds based on investigation capacity and the relative costs of missed fraud and false alerts. Use temporal holdout and confidence intervals where possible.
