#class chapter

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now setting.")

    def roll_over(self):
        print(f'{self.name} rolled over!its age is {self.age}. ')

d = Dog('bunti',3)
d.sit()
d.roll_over()
