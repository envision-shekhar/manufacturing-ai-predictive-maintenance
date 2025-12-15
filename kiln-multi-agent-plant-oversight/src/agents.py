
# src/agents.py
class AnomalyAgent:
    def analyze(self, sample: dict):
        issues = []
        if sample['co'] > 0.4: issues.append('CO spike')
        if abs(sample['setpoint_dev']) > 20: issues.append('Setpoint deviation high')
        if sample['wear_index'] > 0.7: issues.append('Refractory wear high')
        return issues

class MaintenanceAgent:
    def plan(self, anomalies: list[str]):
        plan = []
        if 'Refractory wear high' in anomalies:
            plan.append('Schedule refractory inspection within 24h')
        if 'CO spike' in anomalies:
            plan.append('Check burners and airflow dampers')
        if 'Setpoint deviation high' in anomalies:
            plan.append('Tune PID and verify sensor calibration')
        return plan

class QCAdvisor:
    def recommend(self, anomalies: list[str]):
        recs = []
        if 'CO spike' in anomalies:
            recs.append('Increase excess air slightly and stabilize ramp rates')
        if 'Setpoint deviation high' in anomalies:
            recs.append('Reduce ramp to 8°C/min and validate load distribution')
        return recs
