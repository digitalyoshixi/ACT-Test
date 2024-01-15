import math
import statistics
import numpy as np
data = [72.38, 98.32, 51.7, 144.2, 65.55, 78.66, 65.55, 104.87, 51.7, 41.36, 85.21, 41.36, 91.76, 94, 85.21, 54.79, 65.55, 78.66, 72.1, 41.36, 65.55, 72.1, 72.1, 85.22, 78.66, 67.21, 78.66, 85.21, 85.21, 58.99, 72.1, 78.66, 78.66, 65.5, 65.5]


print("Mean: ",np.mean(data))
print("Mode: ",statistics.mode(data))
print("Median: ", np.median(data))
print("STD: ", np.std(data))
print("Variance: ",np.std(data)**2)
percentile25 = np.percentile(data,25)
percentile75 = np.percentile(data,75)
iqr = percentile75-percentile25
print("Percentile 25% | Quartile 1: ",percentile25)
print("Percentile 75% | Quartile 3: ",percentile75)
print("IQR: ",iqr)
