import numpy as np

# Temperature data collected by meteorologist (in °C)
temperature = np.array([30, 32, 31, 29, 35, 34, 33])

# Statistical calculations
mean_temp = np.mean(temperature)
median_temp = np.median(temperature)
variance_temp = np.var(temperature)
std_dev_temp = np.std(temperature)

# Display results
print("Temperature Data:", temperature)
print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Variance:", variance_temp)
print("Standard Deviation:", std_dev_temp)