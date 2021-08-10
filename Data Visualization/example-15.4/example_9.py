## Modified random walk : 15.4

import random
class RandomWalk:
    def __init__(self,points =1000):
        self.points = points

        # starting point
        self.x_value = [0]
        self.y_value =[0]

    def fill_walk(self):

        while len(self.x_value) <self.points:
            x_dir= random.choice([1])
            x_dis = random.choice([x for x in range(0,8)])
            x_step = x_dir*x_dis

            y_dir = random.choice([1])
            y_dis = random.choice([y for y in range(0,8)])
            y_step = y_dir*y_dis

            if x_step and y_step ==0:
                continue
            self.x_value.append(self.x_value[-1]+x_step)
            self.y_value.append(self.y_value[-1] + y_step)

