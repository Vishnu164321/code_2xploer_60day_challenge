import random
import pandas as pd
import numpy as np
import math


def generate_data(n=18):
    data = []
    for i in range(1, n + 1):
        record = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)

    # Test cases (extreme conditions)
    data.append({"zone": n + 1, "traffic": 0, "air_quality": 50, "energy": 100})  # zero traffic
    data.append({"zone": n + 2, "traffic": 90, "air_quality": 280, "energy": 450})  # extreme pollution
    data.append({"zone": n + 3, "traffic": 20, "air_quality": 50, "energy": 480})  # energy spike

    return data


def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"


def calculate_risk(record):
    score = (record["traffic"] * 0.4 + record["air_quality"] * 0.4 + record["energy"] * 0.2)
    return math.sqrt(score)


def custom_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def detect_patterns(df):
    patterns = {}

    threshold = df["risk_score"].mean()
    patterns["multi_factor_risk"] = df[(df["risk_score"] > threshold) & (df["air_quality"].diff() > 0)
                                       ]
    variance = np.var(df["traffic"])
    patterns["stability"] = "Stable" if variance < 500 else "Unstable"

    high_risk_zones = df[df["category"] == "High Risk"]["zone"].values
    clusters = []
    temp = []

    for z in high_risk_zones:
        if not temp or z == temp[-1] + 1:
            temp.append(z)
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = [z]

    if len(temp) > 1:
        clusters.append(temp)

    patterns["clusters"] = clusters

    return patterns


# MAIN PROGRAM

roll_number = 24110011146

data = generate_data()

for d in data:
    d["category"] = classify_zone(d)
    d["risk_score"] = calculate_risk(d)

if roll_number % 3 == 0:
    random.shuffle(data)
else:
    data = custom_sort(data, "traffic")

df = pd.DataFrame(data)

mean_values = np.mean(df[["traffic", "air_quality", "energy"]], axis=0)

sorted_by_risk = custom_sort(data.copy(), "risk_score")
top3 = sorted_by_risk[-3:]

risk_tuple = (
    df["risk_score"].max(),
    df["risk_score"].mean(),
    df["risk_score"].min()
)

patterns = detect_patterns(df)

avg_risk = risk_tuple[1]

if avg_risk < 10:
    decision = "City Stable"
elif avg_risk < 15:
    decision = "Moderate Risk"
elif avg_risk < 20:
    decision = "High Alert"
else:
    decision = "Critical Emergency"

print("\n--- DATAFRAME ---")
print(df)

print("\n--- MEAN VALUES ---")
print(mean_values)

print("\n--- TOP 3 RISK ZONES ---")
for z in top3:
    print(z)

print("\n--- RISK STATS (max, avg, min) ---")
print(risk_tuple)

print("\n--- PATTERNS DETECTED ---")
print(patterns)

print("\n--- FINAL DECISION ---")
print(decision)
