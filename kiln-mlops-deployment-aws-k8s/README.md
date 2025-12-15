
# MLOps Deployment (AWS + Kubernetes) for Kiln Predictive Maintenance

Reference implementation for packaging the PM model as a web service, containerizing via Docker, and deploying to **Kubernetes**. Includes GitHub Actions CI, a basic Helm chart, and API stubs.

> This repo provides manifests and stubs. Plug in the trained model artifact from `kiln-predictive-maintenance-ml`.

## Components
- FastAPI inference service (`src/api.py`).
- Dockerfile and K8s Deployment/Service manifests (`k8s/`).
- Helm chart for parameterized deploy (`helm/`).
- GitHub Actions CI for build/test.

## Quickstart (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

## Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## Security
- Example NetworkPolicy and resource requests/limits.
- Ready for Zero Trust additions (mTLS, service identities).
