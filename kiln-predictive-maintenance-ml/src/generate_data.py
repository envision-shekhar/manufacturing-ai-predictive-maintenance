
# src/generate_data.py
import numpy as np
import pandas as pd
import argparse
np.random.seed(42)

# Synthetic data generator approximating kiln sensor behavior
# Failure increases with extreme temps, high vibration, high CO, large setpoint deviation, and wear index

def generate(rows: int):
    temp = np.random.normal(1200, 80, rows)  # deg C
    pressure = np.random.normal(3.5, 0.4, rows)  # bar
    vibration = np.random.gamma(2.0, 0.8, rows)
    o2 = np.clip(np.random.normal(6.0, 1.0, rows), 0, 21)
    co = np.clip(np.random.normal(0.25, 0.08, rows), 0, 2)
    airflow = np.random.normal(2500, 250, rows)  # m^3/h
    setpoint_dev = np.random.normal(0.0, 15.0, rows)  # deg C deviation
    wear_index = np.clip(np.random.normal(0.5, 0.2, rows), 0, 1)
    humidity = np.clip(np.random.normal(45, 8, rows), 5, 95)
    feed_rate = np.random.normal(500, 50, rows)  # kg/h

    # Failure logic: sigmoid of weighted sum + noise
    z = (
        0.004*(temp-1150) +
        0.6*(wear_index) +
        0.8*(co) +
        0.02*np.abs(setpoint_dev) +
        0.03*(vibration) +
        -0.001*(airflow-2500) +
        0.0005*(humidity-50) +
        0.0004*(feed_rate-500)
    )
    prob_fail = 1/(1+np.exp(-z))
    failure = (np.random.uniform(0,1, rows) < prob_fail).astype(int)

    df = pd.DataFrame({
        'temperature': temp,
        'pressure': pressure,
        'vibration': vibration,
        'o2': o2,
        'co': co,
        'airflow': airflow,
        'setpoint_dev': setpoint_dev,
        'wear_index': wear_index,
        'humidity': humidity,
        'feed_rate': feed_rate,
        'failure': failure
    })
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, default=20000)
    parser.add_argument('--out', type=str, default='data/sensors.csv')
    args = parser.parse_args()
    df = generate(args.rows)
    import os
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    df.to_csv(args.out, index=False)
    print(f"Saved {args.out} ({len(df)} rows)")
