import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
# square = ([n**2 for n in range(1,6)])
square =[1,4,9,16,25]
plt.plot(input_values,square,linewidth =5)

# Set chart title and label axes.
plt.title("Square Numbers\n",fontsize=24)
plt.xlabel('value',fontsize =14)
plt.ylabel("Square of value", fontsize =14)

# set size of tick labels.
plt.tick_params(axis='both',labelsize =14)
plt.show()
