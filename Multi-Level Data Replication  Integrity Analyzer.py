import random
import numpy as np
import pandas as pd
import math
def generate_data(n):
    data = []
    for i in range(n):
        record = {
            "zone": i + 1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)
    return data

def classify(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk(row):
    score = (row["traffic"] * 0.4 +
             row["air_quality"] * 0.4 +
             row["energy"] * 0.2)
    return score

def manual_sort(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] < data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

city_data = generate_data(18)
for item in city_data:
    item["category"] = classify(item)

random.shuffle(city_data)
df = pd.DataFrame(city_data)
df["risk_score"] = df.apply(calculate_risk, axis=1)

df["risk_log"] = df["risk_score"].apply(lambda x: math.log(x + 1))

matrix = df[["traffic", "air_quality", "energy"]].values

mean_values = np.mean(matrix, axis=0)
sorted_list = manual_sort(city_data, "traffic")
top3 = sorted_list[:3]
max_risk = df["risk_score"].max()
avg_risk = df["risk_score"].mean()
min_risk = df["risk_score"].min()

summary = (max_risk, avg_risk, min_risk)

threshold = avg_risk

high_risk_count = 0
for r in df["risk_score"]:
    if r > threshold:
        high_risk_count += 1

variance = np.var(df["traffic"])

if high_risk_count > 10:
    decision = "Critical Emergency"
elif high_risk_count > 6:
    decision = "High Alert"
elif variance < 500:
    decision = "City Stable"
else:
    decision = "Moderate Risk"


print("\nDataFrame:\n", df)

print("\nMean Values (Traffic, AQI, Energy):", mean_values)

print("\nTop 3 Worst Zones (by traffic):")
for z in top3:
    print(z)

print("\nSummary (max, avg, min risk):", summary)

print("\nFinal Decision:", decision)
