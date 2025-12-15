Predictive Maintenance for Kiln Operations – End-to-End AI Lifecycle
Overview
This project demonstrates how AI and Industry 4.0 principles can transform kiln operations in ceramic brick manufacturing. Inspired by a real-world case at Manufacturing Ltd., it covers the full AI lifecycle:

Problem: Unplanned kiln downtime caused 15–20% production losses annually.
Goal: Predict failures, improve uptime by 20%, reduce maintenance costs, and enhance product quality.
Solution: AI-driven predictive maintenance integrated with Siemens OpCenter MES, IoT sensors, and video analytics.

Lifecycle Stages & Repositories
1. Data & Model Development
Repo: kiln-predictive-maintenance-ml

Generates synthetic kiln sensor data (temperature, pressure, vibration, CO/O₂, airflow, refractory wear index).
Trains supervised ML model (XGBoost or GradientBoosting) for failure prediction.
Outputs metrics (accuracy, precision, recall, ROC-AUC) and serialized model artifact.

Quick Start:
python src/generate_data.py --rows 50000 --out data/sensors.csv
python src/train.py --data data/sensors.csv --model models/kiln_model.pkl
python src/infer.py --model models/kiln_model.pkl --sample-count 5

2. Explainability & Root-Cause Analysis
Repo: kiln-rag-explainability

Implements RAG (Retrieval-Augmented Generation) for answering “why” questions about kiln anomalies.
Uses MES manuals/SOPs as context (synthetic docs provided).
Minimal TF-IDF retriever + placeholder LLM (swap with LangChain/Azure OpenAI easily).

Quickstart:
python src/app.py --question "Why did CO spike during the last firing cycle?"

3. Deployment (MLOps)
Repo: kiln-mlops-deployment-aws-k8s

Wraps the trained model in a FastAPI service.
Provides Dockerfile, Kubernetes manifests, and Helm chart for AWS deployment.
Includes GitHub Actions CI/CD pipeline.

Quickstart:
uvicorn src.api:app --host 0.0.0.0 --port 8000
kubectl apply -f k8s/deployment.yaml

4. Monitoring & Drift Detection
Repo: kiln-monitoring-drift-prometheus

Real-time drift detection using statistical checks (z-score proxy for KS).
Prometheus exporter for sensor metrics.
Sample Prometheus config included.

Quickstart:
python src/exporter.py --port 9000 --data data/sensors_sample.csv

5. Scaling with Multi-Agent Systems
Repo: kiln-multi-agent-plant-oversight

Demonstrates multi-agent orchestration for plant oversight.
Agents: Anomaly detection, maintenance scheduler, QC advisor.
Extensible for mortar mixing lines and other processes.

Quickstart:
python src/run.py

Tech Stack

ML: Python, Pandas, Scikit-learn, XGBoost
GenAI: LangChain-ready RAG pipeline (placeholder LLM included)
Deployment: FastAPI, Docker, Kubernetes, Helm
Monitoring: Prometheus exporter
Security: ISO 27001-aligned scaffolds (env secrets, redaction, audit logs)

Business Impact (Case Study Results)

Downtime reduced: 25% (uptime improved to 95%)
Maintenance cost savings: ₹50 lakhs annually
Quality consistency: +18% (fewer rejects)

Compliance & Safety

Synthetic data used for demos.
Redaction utilities included for sensitive info.
Secrets managed via .env (never commit real keys).

How to Use

Clone this repo or download the bundle ZIP.
Navigate to each sub-repo and follow its README.
Replace synthetic data with your MES/IoT streams for production.
Deploy using provided Kubernetes manifests or Helm charts.

Roadmap

Add LangChain + FAISS for RAG pipeline.
Integrate Prometheus alerts with Alertmanager.
Build operator dashboard for multi-agent decisions.
Add Azure OpenAI integration for explainability.

Contributing
Pull requests welcome! For major changes, open an issue first to discuss what you’d like to change.

Contact
Shekhar Chatterjee
GenAI Solution Architect
envision.shekhar@gmail.com
