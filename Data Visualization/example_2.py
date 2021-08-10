# scatter_squares
import matplotlib.pyplot as plt

filename = r"E:\python_oop\book\crash_course\Data Visualization\Images"
x_value =[n for n in range(1,1001)]
y_value =[i**2 for i in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Greens,edgecolor='none',s=40)

# Set chart title and label axis.
plt.title("Square Number\n", fontsize =24)
plt.xlabel('Values',fontsize = 14)
plt.ylabel('Square Numbers', fontsize = 14)
plt.tick_params(axis='both',which ='major', labelsize =14)

# Set range for each axis.
plt.axis([0,1100,0,1100000])
plt.savefig(f'{filename}\square_plot.png',bbox_inches ='tight')
