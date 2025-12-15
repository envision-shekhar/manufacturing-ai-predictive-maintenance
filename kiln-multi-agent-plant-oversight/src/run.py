
# src/run.py
from agents import AnomalyAgent, MaintenanceAgent, QCAdvisor
from state import PlantState

if __name__ == '__main__':
    state = PlantState()
    anomalies = AnomalyAgent().analyze(state.sample())
    plan = MaintenanceAgent().plan(anomalies)
    advice = QCAdvisor().recommend(anomalies)
    print("Anomalies:", anomalies)
    print("Maintenance Plan:", plan)
    print("QC Advice:", advice)
