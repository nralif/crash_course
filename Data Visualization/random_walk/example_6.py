# addintion example 5
# second part

import matplotlib.pyplot as plt

from example_5 import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.

    rw = RandomWalk(50000)
    rw.fill_walk()
    # set the size of the plotting window
    plt.figure(dpi=128, figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c = point_numbers , cmap =plt.cm.Greens,edgecolor='none',s =40)

    # Emphasize the first and last points.
    plt.scatter(0,0,c='indigo',edgecolor= 'none', s =100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s =100)

    # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_runing = input("Make another walk? (y/n): ")
    if keep_runing in ('n','no','N','NO'):
        break