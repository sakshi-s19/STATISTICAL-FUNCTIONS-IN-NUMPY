import numpy as np

# Weekly rainfall data in mm
rainfall = np.array([12, 15, 20, 18, 25, 10, 22])

# Calculate standard deviation
std_dev = np.std(rainfall)

print("Weekly Rainfall Data:", rainfall)
print("Standard Deviation:", std_dev)