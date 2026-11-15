from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.sentinelpay.predict import predict_one

app = FastAPI(title="SentinelPay API", version="0.1.0",
              description="Synthetic-data educational fraud-risk scoring API.")

class Transaction(BaseModel):
    transaction_id: str = "DEMO-001"
    amount: float = Field(ge=0)
    device_new: int = Field(ge=0, le=1)
    beneficiary_new: int = Field(ge=0, le=1)
    transactions_last_10m: int = Field(ge=0)
    avg_amount_30d: float = Field(gt=0)
    geo_distance_km: float = Field(ge=0)
    failed_attempts_1h: int = Field(ge=0)

@app.get("/health")
def health():
    return {"status":"ok","mode":"synthetic_demo"}

@app.post("/score")
def score(tx: Transaction):
    try:
        result = predict_one(tx.model_dump())
        result["transaction_id"] = tx.transaction_id
        return result
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model not trained. Run scripts/train_model.py")
