#9.4

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.name} Restaurant.\nThis is {self.type} restaurant")

    def open_restaurant(self):
        print(f"The {self.name} is now open.")

    def update_served_number(self):
        print(f"we already served {str(self.number_served)}.")
    def set_number_served(self,served):
        if served>=self.number_served:
            self.number_served = served
        else:
            print('there has no served at this moment')

    def increment_number_server(self,serve):
        self.number_served+= serve
r = Restaurant('alif','5 star')
r.set_number_served(23)
r.update_served_number()
r.increment_number_server(7)
r.update_served_number()
