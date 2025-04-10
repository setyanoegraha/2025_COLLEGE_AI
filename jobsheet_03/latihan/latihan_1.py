# 1. Central Tendency
import numpy as np
from scipy import stats

# a. Mendapatkan Nilai Mean
score = [90, 80, 70, 65, 110, 80, 83, 67, 94]
x = np.mean(score)
print(f"Mean: {x:.2f}")

# b. Mendapatkan Nilai Median
score = [90, 80, 70, 65, 110, 80, 83, 67, 94]
x = np.median(score)
print(f"Median: {x:.2f}")

# c. Mendapatkan Nilai Modus / Mode
score = [90, 80, 70, 65, 110, 80, 83, 67, 94]
x = stats.mode(score, keepdims=True)
print(f"Mode: {x.mode[0]}")
