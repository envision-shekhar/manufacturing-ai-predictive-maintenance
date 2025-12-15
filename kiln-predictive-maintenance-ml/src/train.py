
# src/train.py
import argparse, os, json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score, confusion_matrix

# Try XGBoost; fallback to GradientBoosting
try:
    from xgboost import XGBClassifier
    USE_XGB = True
except Exception:
    from sklearn.ensemble import GradientBoostingClassifier as XGBClassifier
    USE_XGB = False


def train(data_path: str, model_path: str):
    df = pd.read_csv(data_path)
    X = df.drop('failure', axis=1)
    y = df['failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = XGBClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    pr, rc, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
    try:
        auc = roc_auc_score(y_test, y_pred)
    except Exception:
        auc = None
    cm = confusion_matrix(y_test, y_pred).tolist()

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    import pickle
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    os.makedirs('artifacts', exist_ok=True)
    metrics = {
        'use_xgboost': USE_XGB,
        'accuracy': acc,
        'precision': pr,
        'recall': rc,
        'f1': f1,
        'roc_auc': auc,
        'confusion_matrix': cm
    }
    with open('artifacts/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data/sensors.csv')
    parser.add_argument('--model', type=str, default='models/kiln_model.pkl')
    args = parser.parse_args()
    train(args.data, args.model)
