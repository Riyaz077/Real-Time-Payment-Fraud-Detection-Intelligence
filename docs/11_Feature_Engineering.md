# Feature Engineering
Starter features include:
- `amount_to_avg_ratio`: current amount divided by historical average.
- `high_amount_flag`: amount above a chosen threshold.
- `velocity_flag`: elevated recent transaction count.
- `new_device_flag` and `new_beneficiary_flag`.
- `geo_distance_km` and `failed_attempts_1h`.

For a stronger study, calculate rolling counts and sums per sender using event-time windows, enforce strict point-in-time correctness, and compare feature sets through ablation experiments.
