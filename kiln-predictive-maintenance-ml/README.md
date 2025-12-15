
# Predictive Maintenance for Kiln Operations (Ceramic Brick Production)

This repository contains a runnable **predictive maintenance demo** for kiln operations inspired by Maithan Ceramics Ltd.'s Industry 4.0 initiative. It demonstrates data prep, model training (Gradient Boosting as default; XGBoost optional), and inference for **failure prediction** using synthetic sensor data.

> **Note:** The dataset here is **synthetic** for demonstration. Replace with your MES/IoT exports when deploying. The approach mirrors an end-to-end lifecycle: data aggregation, feature engineering, supervised learning, evaluation, and basic MLOps hooks.

## Key Features
- Sensor schema for kiln: temperature, pressure, vibration, gas mix (O2/CO), airflow, setpoint deviation, refractory wear index, ambient humidity, feed rate.
- Train/test split (80/20) with reproducible seeds.
- Metrics: accuracy, precision/recall, ROC-AUC; confusion matrix plot.
- CLI scripts: `generate_data.py`, `train.py`, `infer.py`.
- Minimal experiment tracking (`artifacts/metrics.json`).

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/generate_data.py --rows 50000 --out data/sensors.csv
python src/train.py --data data/sensors.csv --model models/kiln_model.pkl
python src/infer.py --model models/kiln_model.pkl --sample-count 5
```

## Requirements
- Python 3.11+
- Packages in `requirements.txt`. If `xgboost` is not available, code falls back to `sklearn.ensemble.GradientBoostingClassifier`.

## Security & Governance
- No sensitive data; synthetic only.
- .env support for future secrets (e.g., S3 paths).

## Results (sample)
- Expect demo accuracy \> 0.85 on synthetic data.

## Roadmap
- Integrate with real MES (Siemens OpCenter) via APIs.
- Add Prometheus exporters for live drift checks.
- Containerize (Docker) and deploy to Kubernetes.
