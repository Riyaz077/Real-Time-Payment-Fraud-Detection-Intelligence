from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, average_precision_score, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from .feature_engineering import build_features, FEATURES

def train(csv_path="data/sample/sample_transactions.csv", model_dir="models"):
    df = pd.read_csv(csv_path)
    X = build_features(df)[FEATURES]
    y = df["is_fraud"].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=250, min_samples_leaf=2,
                                   class_weight="balanced_subsample",
                                   random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    probs = model.predict_proba(X_test)[:,1]
    preds = (probs >= .5).astype(int)
    metrics = {
        "average_precision": float(average_precision_score(y_test, probs)),
        "roc_auc": float(roc_auc_score(y_test, probs)),
        "classification_report": classification_report(y_test, preds, zero_division=0)
    }
    iso = IsolationForest(contamination="auto", random_state=42)
    iso.fit(X_train)
    Path(model_dir).mkdir(parents=True, exist_ok=True)
    joblib.dump({"model":model,"isolation_forest":iso,"features":FEATURES},
                Path(model_dir)/"sentinelpay_model.joblib")
    return metrics

if __name__ == "__main__":
    print(train())
