import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

x1 = [-2,2]
y1 = [-4,4]

x2 = [-2,2]
y2 = [0.5,2.5]

fig,ax = plt.subplots()

ax.axhline(y=0, c='black')
ax.axvline(x=0, c='black')

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

# ax.xaxis.set_minor_locator(MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(MultipleLocator(0.5))

# ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.5, color='black')
# ax.yaxis.grid(True, which='both', linestyle='--', linewidth=0.5, color='black')
ax.grid(True)

# ax.axis('equal')

ax.plot(x1,y1,label="y1")
ax.plot(x2,y2,label="y2")

ax.set_xlim(-2,2)
ax.set_ylim(-4,4)

ax.legend()
ax.set_title("Row Picture", fontsize=12, fontweight='bold')

plt.show()