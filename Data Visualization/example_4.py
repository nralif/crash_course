# 15.2 colored cubes

import matplotlib.pyplot as plt

filename = r"E:\python_oop\book\crash_course\Data Visualization\Images"

x_value = [x for x in range(1, 5001)]
y_value = [y**3 for y in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, s=200)

# set chart title and label.
plt.title("Cube Numbers\n", fontsize=24)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Cube values', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# set axis for each a value

plt.axis([0, 5000, 0, 125000000000])
plt.savefig(f'{filename}\ex[15.2]_colored_cubes.png', bbox_inches='tight')
plt.show()