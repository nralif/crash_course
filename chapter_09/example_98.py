#9.14
import random
import time
class Dice:
    def __init__(self,sides=6):
        self.sides =sides

    def roll_die(self):
        count = 10
        while count>0:
            result_dice = random.randint(1,6)
            print(result_dice,end=',')
            count-=1
            time.sleep(.3)

d= Dice()
d.roll_die()