
# Monitoring & Drift Detection (Prometheus + Statistical Tests)

Implements **real-time drift detection** for kiln sensors and model outputs. Includes a Prometheus exporter and Kolmogorov–Smirnov/Population Stability Index examples.

## Features
- `exporter.py`: exposes metrics at `/metrics` (Flask-free, simple HTTP server).
- Drift tests over sliding windows; triggers logs and example alerts.
- Prometheus `prometheus.yml` sample scrape config.

## Quickstart
```bash
python src/exporter.py --port 9000 --data data/sensors_sample.csv
```
