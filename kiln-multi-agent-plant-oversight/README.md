
# Multi-Agent Plant Oversight (Kiln + Mortar Lines)

Simplified **multi-agent** orchestration for plant operations: anomaly detection agent, maintenance scheduler, and QC advisor. Demonstrates message passing and decisioning without external frameworks.

## Agents
- `AnomalyAgent`: consumes sensor summaries and flags issues.
- `MaintenanceAgent`: schedules inspections based on wear and deviations.
- `QCAdvisor`: suggests process tweaks (airflow, ramp rates).

## Quickstart
```bash
python src/run.py
```
