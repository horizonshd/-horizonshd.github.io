import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
gammaList = [0.04, 0.1, 0.2, 0.4, 0.67, 1, 1.5, 2.5, 5, 10, 25]
x = np.arange(0.0, 255.0, 0.01)
yList = [np.power(x/255,gamma) * 255 for gamma in gammaList]

labelX = [20,40,60,80,100,120,140,160,185,210,230]
labelY = [math.pow(labelX[i]/255,gammaList[i]) * 255 for i in  range(len(gammaList))]
angleList = [10, 15, 20, 30, 40, 45, 47, 49, 51, 53, 55]
colorList = ['#1717FF', '#188C18', '#FF1717', '#1AC5C5', '#C720C7', '#C8C824', '#353535', '#3838FF', '#259225', '#FF1D1D', '#26C9C9']

for i in range(len(yList)):
    plt.plot(x, yList[i],colorList[i])
    plt.text(labelX[i], labelY[i], r'$\gamma = $' + str(gammaList[i]), color = colorList[i], rotation = angleList[i] , va='center', ha='center',backgroundcolor='w')

plt.xlabel('Input value')
plt.ylabel('Output value')
plt.title('Plot for different values of gamma', fontsize=12, fontweight='bold')

# fig.savefig("test.png")
plt.show()