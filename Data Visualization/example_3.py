# cubes: 15.1
import matplotlib.pyplot as plt

filename = r"E:\python_oop\book\crash_course\Data Visualization\Images"

x_value = [n for n in range(1,5001)]
y_value = [n**3 for n in x_value]

plt.scatter(x_value,y_value,s=200)

# set chart title and label.
plt.title("Cubes Number", fontsize =24)
plt.xlabel("values",fontsize = 14)
plt.ylabel("cubes value",fontsize =14)
plt.tick_params(axis='both',which ='major', labelsize = 10)

# set axis for each value.
plt.axis([0,5000,0,125000000000])

plt.savefig(f'{filename}\ex[15.1]_cubes.png',bbox_inches ='tight')
plt.show()