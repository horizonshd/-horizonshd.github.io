import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from functools import partial

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

ax.axis('equal')

ax.set_ylim(-2,4)

arrow_vector = partial(plt.arrow, width=0.01, head_width=0.1, head_length=0.2, length_includes_head=True)

arrow_vector(0, 0, 2, -1, color='g')
arrow_vector(0, 0, -1, 2, color='c')
arrow_vector(2, -1, -2, 4, color='b')
arrow_vector(0, 0, 0, 3, width=0.05, color='r')

ax.set_title("Column Picture", fontsize=12, fontweight='bold')

plt.show()