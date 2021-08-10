#9.1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.name}.\nThis is {self.type} restaurant")

    def open_restaurant(self):
        print(f"The {self.name} is now open.")

r = Restaurant('alif restaurant','5 star')
print(r.name)
print(r.type)
r.describe_restaurant()
r.open_restaurant()

