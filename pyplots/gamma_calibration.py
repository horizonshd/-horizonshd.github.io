import matplotlib.pyplot as plt
import numpy as np

# Data for plotting

x = np.arange(0.0, 255.0, 0.01)
y1 = np.power(x/255,0.04) * 255
y2 = np.power(x/255,0.1) * 255
y3 = np.power(x/255,0.2) * 255
y4 = np.power(x/255,0.4) * 255
y5 = np.power(x/255,0.67) * 255
y6 = np.power(x/255,1) * 255
y7 = np.power(x/255,1.5) * 255
y8 = np.power(x/255,2.5) * 255
y9 = np.power(x/255,5) * 255
y10 = np.power(x/255,10) * 255
y11 = np.power(x/255,25) * 255

fig, ax = plt.subplots()
l1 = ax.plot(x, y1, label = '0.04')
l2 = ax.plot(x, y2)
l3 = ax.plot(x, y3)
l4 = ax.plot(x, y4)
l5 = ax.plot(x, y5)
l6 = ax.plot(x, y6)
l7 = ax.plot(x, y7)
l8 = ax.plot(x, y8)
l9 = ax.plot(x, y9)
l10 = ax.plot(x, y10)
l11 = ax.plot(x, y11)

plt.setp(l1, color='#1717FF')
plt.setp(l2, color='#188C18')
plt.setp(l3, color='#FF1717')
plt.setp(l4, color='#1AC5C5')
plt.setp(l5, color='#C720C7')
plt.setp(l6, color='#C8C824')
plt.setp(l7, color='#353535')
plt.setp(l8, color='#3838FF')
plt.setp(l9, color='#259225')
plt.setp(l10, color='#FF1D1D')
plt.setp(l11, color='#26C9C9')

plt.text(20, 230.3, r'$\gamma = 0.04$', color = '#1717FF', rotation = 10 , va='center', ha='center',backgroundcolor='w')
plt.text(40, 211.9, r'$\gamma = 0.1$', color = '#188C18', rotation = 15 , va='center', ha='center', backgroundcolor='w')
plt.text(60, 190.9, r'$\gamma = 0.2$', color = '#FF1717', rotation = 20 , va='center', ha='center', backgroundcolor='w')
plt.text(80, 160.4, r'$\gamma = 0.4$', color = '#1AC5C5', rotation = 30 , va='center', ha='center', backgroundcolor='w')
plt.text(100, 136.2, r'$\gamma = 0.67$', color = '#C720C7', rotation = 40 , va='center', ha='center', backgroundcolor='w')
plt.text(120, 120, r'$\gamma = 1$', rotation = 45 , va='center', ha='center', color = '#C8C824',backgroundcolor='w')
plt.text(140, 103.7, r'$\gamma = 1.5$', rotation = 47 , va='center', ha='center', color = '#353535',backgroundcolor='w')
plt.text(160, 79.5, r'$\gamma = 2.5$', rotation = 49 , va='center', ha='center', color = '#3838FF',backgroundcolor='w')
plt.text(185, 51.3, r'$\gamma = 5$', rotation = 51 , va='center', ha='center', color = '#259225',backgroundcolor='w')
plt.text(210, 36.6, r'$\gamma = 10$', rotation = 53 , va='center', ha='center', color = '#FF1D1D',backgroundcolor='w')
plt.text(230, 19.3, r'$\gamma = 25$', rotation = 55 , va='center', ha='center', color = '#26C9C9',backgroundcolor='w')

# ax.set(xlabel='Input value', ylabel='Output value',
#       title='Plot for different values of gamma')

plt.xlabel('Input value')
plt.ylabel('Output value')
plt.title('Plot for different values of gamma', fontsize=12, fontweight='bold')

# ax.grid()

# fig.savefig("test.png")
plt.show()


