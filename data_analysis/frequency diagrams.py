import numpy as np
import math 
import matplotlib.pyplot as plt
# get frequency table
rawdata = [72.38, 98.32, 51.7, 144.2, 65.55, 78.66, 65.55, 104.87, 51.7, 41.36, 85.21, 41.36, 91.76, 94, 85.21, 54.79, 65.55, 78.66, 72.1, 41.36, 65.55, 72.1, 72.1, 85.22, 78.66, 67.21, 78.66, 85.21, 85.21, 58.99, 72.1, 78.66, 78.66, 65.5, 65.5]
rawdata = np.array(rawdata)
themax = rawdata.max()
themin = rawdata.min()
indices = 10
step = (float(themax)-float(themin))/indices
rangeddata = np.arange(themin,themax,step)
print(rangeddata)
freqchart = []
for i in rangeddata:
    freqchart.append(["{:.1f}".format(i-step/2)+"-"+"{:.1f}".format(i+step/2),0])
for i in rawdata:
    closestnum = len(rangeddata)
    lastdiff = 1000
    for v in range(len(rangeddata)):
        difference = abs(i-rangeddata[v])
        if difference<lastdiff:
            lastdiff=difference
            closestnum=v
    if closestnum!=len(rangeddata):
        freqchart[closestnum][1]+=1

print(len(rawdata))
print(freqchart)

xdata = []
ydata = []
for i in freqchart:
    xdata.append(i[0])
    ydata.append(i[1])

ydata = np.array(ydata)
xdata = np.array(xdata)
plt.bar(xdata,ydata,align='center')
plt.plot(xdata,ydata,c='red')
plt.ylabel('Frequency')
plt.xlabel('Entropy(bits)')
plt.title("Frequency of Entropies")
plt.show()
