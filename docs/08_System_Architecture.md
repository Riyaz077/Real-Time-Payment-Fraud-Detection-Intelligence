# System Architecture
```mermaid
flowchart TD
 A[Synthetic UPI-like Events] --> B[Ingestion and Validation]
 B --> C[Preprocessing]
 C --> D[Behavioural Feature Engineering]
 D --> E[Fraud Classifier]
 D --> F[Anomaly Detector]
 E --> G[Risk Scoring and Reason Codes]
 F --> G
 G --> H[Alert Store]
 G --> I[FastAPI]
 H --> J[Streamlit Analyst Dashboard]
 I --> J
```

### Components
- Generator: creates safe, reproducible synthetic events.
- Preprocessor: validates schema and handles missing values.
- Feature engine: derives velocity, novelty and amount-deviation features.
- Classifier: supervised baseline.
- Anomaly detector: independent outlier signal.
- Risk engine: combines signals using documented weights.
- Alert layer: emits review candidates and reason codes.
- API/dashboard: serving and visualization.

A future deployment may introduce Kafka/Redpanda, a feature store, PostgreSQL, model registry, observability and role-based access controls.
