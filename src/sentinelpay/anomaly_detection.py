# Isolation Forest is fitted in train.py and scored in predict.py.
# Keep this module as the extension point for drift and anomaly analytics.
def anomaly_summary(scores):
    return {"count": len(scores), "mean_score": sum(scores)/len(scores) if scores else 0.0}
