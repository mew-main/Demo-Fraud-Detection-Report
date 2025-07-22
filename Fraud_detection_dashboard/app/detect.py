import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
import numpy as np
import json
from sklearn.ensemble import IsolationForest

def load_config(config_path = "../Fraud_detection_dashboard/config/recurring_config.json"):
    with open(config_path, "r") as f:
        return json.load(f)
#def load_config(config_path=None):
#   if config_path is None:
       #always resolve relative to file's parent
#        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Fraud_detection_dashboard/config","recurring_config.json")
#    with open(config_path, "r") as f:
#        return json.load(f) 

def is_recurring(transaction, config):
    for entry in config:
        if entry["name"].lower() in transaction["description"].lower() and float(transaction["amount"]) <= entry["threshold"]:
            return True
    return False

def detect_anomalies(df, config):
    # Exclude known recurring charges
    mask = df.apply(lambda row: is_recurring(row, config), axis=1)
    df["is_recurring"] = mask
    df_to_check = df[~mask]
    # Use Isolation Forest for anomaly detection
    if len(df_to_check) > 0:
        model = IsolationForest(contamination=0.3, random_state=900)
        df_to_check["anomaly_score"] = model.fit_predict(df_to_check[["amount"]])
        df.loc[df_to_check.index, "anomaly_score"] = df_to_check["anomaly_score"]
        df["flagged"] = df["anomaly_score"] == -1
    else:
        df["anomaly_score"] = 1
        df["flagged"] = False
    return df 