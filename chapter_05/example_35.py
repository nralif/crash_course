# 5.1
import random

car_name =['subaru','audi','marcidis','banch']
car = random.choice(car_name)
# print(car)
for i in range(1,11):
    car = random.choice(car_name)
    if 'subaru' in car:
        print('True')
    else:
        print('False')