def reason_codes(row):
    reasons = []
    if float(row.get("device_new",0)) == 1: reasons.append("NEW_DEVICE")
    if float(row.get("beneficiary_new",0)) == 1: reasons.append("NEW_BENEFICIARY")
    if float(row.get("transactions_last_10m",0)) >= 5: reasons.append("HIGH_TRANSACTION_VELOCITY")
    if float(row.get("amount_to_avg_ratio",0)) >= 4: reasons.append("AMOUNT_ABOVE_CUSTOMER_BASELINE")
    if float(row.get("geo_distance_km",0)) >= 100: reasons.append("UNUSUAL_GEO_DISTANCE")
    if float(row.get("failed_attempts_1h",0)) >= 3: reasons.append("REPEATED_FAILED_ATTEMPTS")
    return reasons or ["MODEL_SIGNAL_REQUIRES_REVIEW"]
