
# src/infer.py
import argparse, pickle
import numpy as np
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='models/kiln_model.pkl')
    parser.add_argument('--sample-count', type=int, default=5)
    args = parser.parse_args()
    with open(args.model, 'rb') as f:
        model = pickle.load(f)
    # Create random samples around nominal values
    rows = []
    for _ in range(args.sample_count):
        rows.append({
            'temperature': np.random.normal(1200, 50),
            'pressure': np.random.normal(3.5, 0.3),
            'vibration': np.random.gamma(2.0, 0.7),
            'o2': np.clip(np.random.normal(6.0, 1.0), 0, 21),
            'co': np.clip(np.random.normal(0.25, 0.06), 0, 2),
            'airflow': np.random.normal(2500, 200),
            'setpoint_dev': np.random.normal(0.0, 10.0),
            'wear_index': np.clip(np.random.normal(0.5, 0.2), 0, 1),
            'humidity': np.clip(np.random.normal(45, 8), 5, 95),
            'feed_rate': np.random.normal(500, 40)
        })
    df = pd.DataFrame(rows)
    preds = model.predict(df)
    print("Samples:")
    print(df)
    print("Predicted failure (1=yes):", preds.tolist())
