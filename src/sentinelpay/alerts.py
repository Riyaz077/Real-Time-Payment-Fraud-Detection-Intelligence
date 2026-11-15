from datetime import datetime, timezone
def create_alert(transaction_id, prediction):
    return {
        "alert_id": f"AL-{transaction_id}",
        "transaction_id": transaction_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "risk_score": prediction["risk_score"],
        "risk_band": prediction["risk_band"],
        "reason_codes": prediction["reason_codes"],
        "status": "PENDING_HUMAN_REVIEW"
    }
