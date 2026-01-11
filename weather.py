import numpy as np

temps = np.array([32, 35, 33, 36, 38, 34, 31])

print("Average Temperature:", np.mean(temps))
print("Highest Temperature:", np.max(temps))
print("Lowest Temperature:", np.min(temps))

hot_days = temps[temps > 35]
print("Hot Days:", hot_days)
