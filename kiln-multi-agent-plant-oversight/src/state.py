
# src/state.py
import numpy as np
class PlantState:
    def sample(self):
        return {
            'temperature': np.random.normal(1200, 60),
            'co': np.clip(np.random.normal(0.25, 0.1), 0, 2),
            'setpoint_dev': np.random.normal(0.0, 18.0),
            'wear_index': np.clip(np.random.normal(0.55, 0.25), 0, 1)
        }
