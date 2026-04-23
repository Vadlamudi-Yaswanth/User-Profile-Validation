import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
def create_student_data(n):
    records = []
    for i in range(n):
        sid = f"S{i+1:03d}"
        m = random.randint(0, 100)
        att = random.randint(0, 100)
        assign = random.randint(0, 50)
        perf_score = math.sqrt(m * assign) + (2 * att) - math.log(m + 1)

        records.append((sid, m, att, assign, perf_score))
    return records


def student_classification(data):
    result = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }
    for rec in data:
        sid, m, att, assign, pi = rec
        if m < 40 or att < 50:
            result["At Risk"].append(sid)

        elif m > 90 and att > 80:
            result["Top Performer"].append(sid)

        elif 71 <= m <= 90:
            result["Good"].append(sid)

        else:
            result["Average"].append(sid)

    return result
def perform_analysis(df):
    marks_vals = df["Marks"].values
    manual_mean = sum(marks_vals) / len(marks_vals)
    median_marks = np.median(marks_vals)
    std_dev_marks = np.std(marks_vals)
    correlation = df["Marks"].corr(df["Attendance"])
    min_marks = min(marks_vals)
    max_marks = max(marks_vals)

    normalized_marks = [
        (x - min_marks) / (max_marks - min_marks)
        for x in marks_vals
    ]

    df["Normalized Marks"] = normalized_marks

    stats_tuple = (manual_mean, std_dev_marks, max_marks)

    return stats_tuple, correlation
def check_system_pattern(df, categories):

    std_dev = np.std(df["Marks"])

    attendance_risk = len(df[df["Attendance"] < 50])

    top_performers = len(categories["Top Performer"])

    if std_dev < 15 and attendance_risk <= 3 and top_performers >= 2:
        return "Stable Academic System"

    elif std_dev < 25:
        return "Moderate Performance"

    else:
        return "Critical Attention Required"
last_digit = int(input("Enter last digit of your roll number: "))

if last_digit == 0:
    last_digit = 10

students = create_student_data(last_digit)

df = pd.DataFrame(
    students,
    columns=[
        "Student_ID",
        "Marks",
        "Attendance",
        "Assignment",
        "Performance_Index"
    ]
)

category_dictionary = student_classification(students)

category_sets = {
    key: set(value)
    for key, value in category_dictionary.items()
}

stats_tuple, correlation_value = perform_analysis(df)

system_status = check_system_pattern(df, category_dictionary)

print("\n===== STUDENT DATAFRAME =====\n")
print(df)

print("\n===== STUDENT CATEGORY DICTIONARY =====\n")
print(category_dictionary)

print("\n===== CATEGORY SET REPRESENTATION =====\n")
print(category_sets)

print("\n===== STATISTICAL SUMMARY TUPLE =====")
print("(Mean, Std Dev, Max Marks)")
print(stats_tuple)

print("\nCorrelation between Marks and Attendance:")
print(correlation_value)

print("\n===== FINAL SYSTEM INSIGHT =====")
print(system_status)
