# 9.2

class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'welcome to {self.name}')


r1 = Restaurant('rahman Restaurant','4 star')
r2 = Restaurant('karim Restaurant','3 star')
r3 = Restaurant('naeem Restaurant','2 star')

print()
r1.describe_restaurant()
print()
r2.describe_restaurant()
print()
r3.describe_restaurant()

