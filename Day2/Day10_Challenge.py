import random
import copy
import math
import numpy as np
import pandas as pd
def generate_data(n):
    students = []
    for i in range(n):
        students.append({
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        })
    return students
def mutate(data, roll_no):
    rule = roll_no % 3

    for i in range(len(data)):
        if i % 3 == rule:
            data[i]["marks"] += math.sqrt(data[i]["marks"])
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 3

def make_df(data):
    return pd.DataFrame(data)

def analyze(original_df, modified_df):
    orig = original_df["marks"]
    mod = modified_df["marks"]

    mean = np.mean(mod)
    std = np.std(mod)
    drift = abs(np.mean(orig) - mean)

    manual_mean = sum(mod) / len(mod)
    modified_df["normalized"] = (mod - min(mod)) / (max(mod) - min(mod))

    return mean, drift, std, manual_mean

def get_status(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"


roll_no = int(input("Enter the Roll No: "))
threshold = 5

students = generate_data(12)

shallow = copy.copy(students)
deep = copy.deepcopy(students)

original_df = make_df(students)

mutate(shallow, roll_no)
mutate(deep, roll_no)

shallow_df = make_df(shallow)
deep_df = make_df(deep)

mean, drift, std, manual_mean = analyze(original_df, deep_df)

status = get_status(drift, threshold, students, shallow)

print("\nOriginal Data:\n", original_df)
print("\nShallow Copy:\n", shallow_df)
print("\nDeep Copy:\n", deep_df)

print("\nDrift:", drift)
print("Tuple:", (mean, drift, std))

print("\nManual Mean:", manual_mean)

print("\nFinal Status:", status)