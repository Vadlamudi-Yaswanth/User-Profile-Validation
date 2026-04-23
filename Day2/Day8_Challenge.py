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
