#book work

class Car:
    def __init__(self,make,model,year):
        self.make =make
        self.model = model
        self.year =year
        self.odomerter_reading = 0

    def get_descriptive_name(self):
        long_name = (f"In {str(self.year)}, the car made {self.make} on model {self.model}.")
        return long_name

    def read_odometer(self):
        print(f"This car has {str(self.odomerter_reading)} miles on it.")

    def update_odometer(self,mileags):
        if mileags >= self.odomerter_reading:
            self.odomerter_reading =mileags
        else:
            print('you can\'t roll back an odometer! ' )

    def increment_odometer(self,miles):
        self.odomerter_reading+=miles

class Battery():
    def __init__(self,battery_size =70):
        self.battery_size = battery_size

    def describe_bettery(self):
        print(f"This car has a {str(self.battery_size)}-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            rang =240
        elif self.battery_size ==85:
            rang = 270
        else:
            print('out of range')

        msg = f"this car can go approximately {str(rang)} miles on a full charge."
        print(msg)
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_ges_tank(self):
        print('this car doesn\'t have gas tanks.'  )

ec = ElectricCar('alif','aN21',2021)
print(ec.get_descriptive_name())
ec.battery.describe_bettery()
ec.battery.get_range()