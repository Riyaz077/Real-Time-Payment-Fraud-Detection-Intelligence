# Project Proposal
## SentinelPay: AI-Powered Real-Time UPI Fraud Detection and Financial Crime Intelligence

### Executive summary
SentinelPay is a research prototype that analyses synthetic UPI-like transaction events to identify potentially fraudulent behaviour. It combines supervised classification, unsupervised anomaly detection, behavioural features, risk scoring, explainable alerts and an analyst dashboard.

### Motivation
Instant digital payments create a need for fast, reliable risk signals. Rule-only systems can be brittle when patterns evolve; machine learning can complement rules by learning interactions among transaction amount, velocity, device novelty and beneficiary behaviour.

### Proposed solution
A modular pipeline ingests events, validates and enriches records, computes behavioural features, scores risk, produces reason codes and presents cases for human review.

### Deliverables
Dataset generator, data dictionary, notebooks, trained baseline, API, dashboard, tests, technical documentation and evaluation report.

### Success criteria
Reproducible execution; leakage-aware evaluation; documented precision/recall trade-offs; understandable reason codes; measured inference latency; and clear limitations.
