
# src/exporter.py
import argparse, time
import numpy as np, pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer

class Metrics:
    def __init__(self, df):
        self.df = df
        self.window = 500
        self.ptr = 0
    def next_batch(self):
        start = self.ptr
        end = min(len(self.df), start + self.window)
        batch = self.df.iloc[start:end]
        self.ptr = 0 if end >= len(self.df) else end
        return batch
    def drift_ks(self, col, ref_mean, ref_std):
        x = self.next_batch()[col].values
        # simple z-score deviation metric as proxy for KS
        z = np.abs((x.mean()-ref_mean)/ref_std)
        return z

class Handler(BaseHTTPRequestHandler):
    metrics: Metrics = None
    def do_GET(self):
        if self.path == '/metrics':
            cols = ['temperature','pressure','vibration','co','airflow','setpoint_dev']
            lines = []
            for c in cols:
                ref_mean = float(self.server.refs[c]['mean'])
                ref_std = float(self.server.refs[c]['std']) or 1.0
                z = self.server.metrics.drift_ks(c, ref_mean, ref_std)
                lines.append(f"kiln_drift_zscore{{sensor='{c}'}} {z}")
            body = "
".join(lines)+"
"
            self.send_response(200)
            self.send_header('Content-Type','text/plain; version=0.0.4')
            self.end_headers()
            self.wfile.write(body.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9000)
    parser.add_argument('--data', type=str, default='data/sensors_sample.csv')
    args = parser.parse_args()
    df = pd.read_csv(args.data)
    refs = df.describe().to_dict()
    metrics = Metrics(df)
    server = HTTPServer(('0.0.0.0', args.port), Handler)
    server.metrics = metrics
    server.refs = refs
    print(f"Serving metrics on :{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
