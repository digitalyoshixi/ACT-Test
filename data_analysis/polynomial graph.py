import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import uncertainties as unc 
from scipy import stats
import uncertainties.unumpy as unp


# win% | round avg | react avg | entropy
x = [1.4296950952380951, 1.0955179285714287, 0.73925748, 0.8304863333333331, 0.6976688400000001, 0.528369, 0.37767555555555554, 0.6232305499999999, 0.6871086666666666, 0.7688437272727273, 0.6944691304347829, 0.6621701600000002, 0.4796866, 0.46927633333333335, 0.41545512, 0.8936162000000002, 0.49201216000000003, 0.49399412000000015, 0.39878256000000006, 0.41465859999999993, 0.41584152, 0.46933408695652173, 0.51413316, 0.7311294166666666, 0.8936057999999999, 0.490286, 0.77560256, 0.6762682272727273, 0.42832000000000003, 0.64255425, 0.5427226999999999, 0.8976946315789477, 0.8944778260869564, 0.4439672666666668, 1.0650873200000002]
y = [72.38, 98.32, 51.7, 144.2, 65.55, 78.66, 65.55, 104.87, 51.7, 41.36, 85.21, 41.36, 91.76, 94, 85.21, 54.79, 65.55, 78.66, 72.1, 41.36, 65.55, 72.1, 72.1, 85.22, 78.66, 67.21, 78.66, 85.21, 85.21, 58.99, 72.1, 78.66, 78.66, 65.5, 65.5]

# graphing
x = np.array(x)
y = np.array(y)

plt.scatter(x, y, color='green')
plt.axis([0, 1.5, 0, 150])
plt.title('Degree 3 Polynomial Regression for ACT Reaction Time and Password Entropy')
plt.ylabel('Entropy(bits)')
plt.xlabel('Reaction Time(s)')


def f(x,a,b,c,d):
  return a*x**3+b*x**2+c*x+d

popt, pcov = curve_fit(f,x,y)

a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]
print('Optimal Values')
print('a: ' + str(a))
print('b: ' + str(b))
print('c: ' + str(c))
print('d: ' + str(d))
newy = f(x,a,b,c,d)
print("r2 score: ",r2_score(y,newy))

a,b,c,d = unc.correlated_values(popt,pcov)
print("uncertainties:")
print(a,"\n",b,"\n",c,"\n",d)

# plot data
plt.scatter(x,y,s=3,label="data")

# calculate regression confidence
px = np.linspace(0,1.5,100)
py = a*px**3+b*px**2+c*px+d
nom = unp.nominal_values(py)
std = unp.std_devs(py)
def predband(x, xd, yd, p, func, conf=0.95):
    # x = requested points
    # xd = x data
    # yd = y data
    # p = parameters
    # func = function name
    alpha = 1.0 - conf    # significance
    N = xd.size          # data sample size
    var_n = len(p)  # number of parameters
    # Quantile of Student's t distribution for p=(1-alpha/2)
    q = stats.t.ppf(1.0 - alpha / 2.0, N - var_n)
    # Stdev of an individual measurement
    se = np.sqrt(1. / (N - var_n) * \
                 np.sum((yd - func(xd, *p)) ** 2))
    # Auxiliary definitions
    sx = (x - xd.mean()) ** 2
    sxd = np.sum((xd - xd.mean()) ** 2)
    # Predicted values (best-fit model)
    yp = func(x, *p)
    # Prediction band
    dy = q * se * np.sqrt(1.0+ (1.0/N) + (sx/sxd))
    # Upper & lower prediction bands.
    lpb, upb = yp - dy, yp + dy
    return lpb, upb

lpb, upb = predband(px, x, y, popt, f, conf=0.95)

# plot the regression
plt.plot(px, nom, c='black', label='y=ax^3+bx^2+cx+d')

# uncertainty lines (95% confidence)
plt.plot(px, nom - 1.96 * std, c='orange',\
         label='95% Confidence Region')
plt.plot(px, nom + 1.96 * std, c='orange')
# prediction band (95% confidence)
plt.plot(px, lpb, 'k--',label='95% Prediction Band')
plt.plot(px, upb, 'k--')
plt.ylabel('Entropy(bits)')
plt.xlabel('Reaction Time(s)')
plt.legend(loc='best')
plt.show()