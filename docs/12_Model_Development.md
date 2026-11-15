# Model Development
## Supervised
Logistic Regression provides a transparent baseline. Random Forest captures nonlinear feature interactions. Consider XGBoost after establishing reliable splits and baselines.

## Unsupervised
Isolation Forest produces an anomaly score independent of fraud labels. It should be treated as a complementary signal, not a fraud probability.

## Reproducibility
Fix random seeds, persist feature lists and preprocessing, record package versions, dataset version/hash and training parameters. Fit every transformation on training data only.
