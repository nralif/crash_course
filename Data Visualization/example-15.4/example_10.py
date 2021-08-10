# 2nd part
import matplotlib.pyplot as plt

from example_9 import RandomWalk


while True:
    # instance
    r = RandomWalk(50000)
    r.fill_walk()

    # figure size
    plt.figure(dpi = 128, figsize=(10,6))
    # main figure
    point = list(range(r.points))
    # plt.scatter(r.x_value,r.y_value,c=point,cmap=plt.cm.Greens,s=1)

    plt.plot(r.x_value,r.y_value,c = 'skyblue',linewidth = 1)
    # start and end point
    plt.scatter(0,0,c='indigo',edgecolors= 'none',s=100)
    plt.scatter(r.x_value[-1],r.y_value[-1],c='red',edgecolors='none',s =100)


    # display none
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    # stop point
    next_plot = input("do you want continue  'y/n'?")
    if next_plot in ('n','no','N','No'):
        continue

