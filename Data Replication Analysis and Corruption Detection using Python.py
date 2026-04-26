import random
import copy
import math
import numpy as np
import pandas as pd

def generate_data(n):
    data = []
    for i in range(n):
        record = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(0, 100),
                "pollution": random.randint(0, 300),
                "energy": random.randint(0, 500)
            },
            "history": [random.randint(10, 100) for _ in range(3)]
        }
        data.append(record)
    return data

def replicate_data(original):
    return original, copy.copy(original), copy.deepcopy(original)

def custom_risk(m):
    base = m["traffic"] + m["pollution"] + m["energy"]
    return math.log(base + 1) * 1.2

def modify_data(data):
    for d in data:
        d["metrics"]["traffic"] += 10
        d["metrics"]["energy"] += 20
        d["history"].append(random.randint(50, 150))

def manual_corr(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    num = 0
    dx = 0
    dy = 0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        dx += (x[i] - x_mean) ** 2
        dy += (y[i] - y_mean) ** 2
    return num / ((dx ** 0.5) * (dy ** 0.5))

data = generate_data(15)

assign_copy, shallow_copy, deep_copy = replicate_data(data)

data.reverse()

df = pd.DataFrame([{
    "zone": d["zone"],
    "traffic": d["metrics"]["traffic"],
    "pollution": d["metrics"]["pollution"],
    "energy": d["metrics"]["energy"]
} for d in data])

df["risk"] = df.apply(lambda r: custom_risk({
    "traffic": r["traffic"],
    "pollution": r["pollution"],
    "energy": r["energy"]
}), axis=1)

traffic_arr = df["traffic"].values
poll_arr = df["pollution"].values

corr_val = manual_corr(traffic_arr, poll_arr)

modify_data(shallow_copy)

df_after = pd.DataFrame([{
    "zone": d["zone"],
    "traffic": d["metrics"]["traffic"],
    "pollution": d["metrics"]["pollution"],
    "energy": d["metrics"]["energy"]
} for d in data])

matrix = df_after[["traffic", "pollution", "energy"]].values

mean_vals = np.mean(matrix, axis=0)
std_vals = np.std(matrix, axis=0)
var_vals = np.var(matrix, axis=0)

anomalies = []
for i in range(len(matrix)):
    if any(matrix[i][j] > mean_vals[j] + std_vals[j] for j in range(3)):
        anomalies.append(i + 1)

risk_scores = df["risk"].values
threshold = np.mean(risk_scores)

risky = []
for i in range(len(risk_scores)):
    if risk_scores[i] > threshold:
        risky.append(i)

clusters = []
temp = []
for i in range(len(risky)):
    if i == 0 or risky[i] == risky[i - 1] + 1:
        temp.append(risky[i])
    else:
        if len(temp) > 1:
            clusters.append(temp)
        temp = [risky[i]]
if len(temp) > 1:
    clusters.append(temp)

stability_index = 1 / (np.mean(var_vals) + 1)

max_risk = np.max(risk_scores)
min_risk = np.min(risk_scores)

summary = (max_risk, min_risk, stability_index)

if len(anomalies) > 7:
    decision = "Critical Failure"
elif len(anomalies) > 4:
    decision = "High Corruption Risk"
elif len(anomalies) > 2:
    decision = "Moderate Risk"
else:
    decision = "System Stable"

print("Before:\n", df)
print("\nAfter:\n", df_after)
print("\nAnomalies:", anomalies)
print("\nSummary:", summary)
print("\nDecision:", decision)