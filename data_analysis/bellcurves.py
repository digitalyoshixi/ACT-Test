import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# Generate some data for this demonstration.
data = [1.4296950952380951, 1.0955179285714287, 0.73925748, 0.8304863333333331, 0.6976688400000001, 0.528369, 0.37767555555555554, 0.6232305499999999, 0.6871086666666666, 0.7688437272727273, 0.6944691304347829, 0.6621701600000002, 0.4796866, 0.46927633333333335, 0.41545512, 0.8936162000000002, 0.49201216000000003, 0.49399412000000015, 0.39878256000000006, 0.41465859999999993, 0.41584152, 0.46933408695652173, 0.51413316, 0.7311294166666666, 0.8936057999999999, 0.490286, 0.77560256, 0.6762682272727273, 0.42832000000000003, 0.64255425, 0.5427226999999999, 0.8976946315789477, 0.8944778260869564, 0.4439672666666668, 1.0650873200000002]

# Fit a normal distribution to the data:
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=33, density=True, alpha=0.6, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
print("Fit results: mu = %.2f,  std = %.2f" % (mu, std))
plt.xlabel("Reaction Speed(s)")
plt.ylabel("Frequency")
plt.title("Histogram/Bellcurve for Freqency of Reaction Speeds")

plt.show()