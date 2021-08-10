# Refactoring : 15.5
import random

class RandomWalk:
    def __init__(self,number_points = 50000):
        self.number_points = number_points

        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        while True:
            if x_steps and y_steps ==0:
                continue
            x_steps = RandomWalk.get_step(self)
            y_steps = RandomWalk.get_step(self)
    def get_step(self):
        global x_steps,y_steps
        x_dir = random.choice([1,-1])
        x_dis = random.choice([x for x in range(0,11)])
        x_steps = x_dir*x_dis

        y_dir = random.choice([1,-1])
        y_dis = random.choice([y**2 for y in range(0,11)])
        y_steps = y_dis*y_dir


        next_x = self.x_value[-1]+x_steps
        next_y = self.y_value[-1]=y_steps
        self.x_value.append(next_x)
        self.y_value.append(next_y)

