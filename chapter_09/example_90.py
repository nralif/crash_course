#9.3

class User:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def describe_user(self,**others_info):
        information = {}
        for name, info in others_info.items():
            information[name] = info
        print('your info:')
        print(f"\tFull Name: {self.fname} {self.lname}")
        for name,value in information.items():
            print(f"\t{name}: {value}")

    def greet_user(self):
        print(f"Hi {self.fname}. Have a nice day.")
u1 = User('naeemur','rahman')
u2 = User('arifur','rahman')
u3 = User('kabir','sing')
u1.describe_user( age =21, color='gray white'),u1.greet_user()
print()
u2.describe_user(age =31,color='light dark'),u2.greet_user()
print()
u3.describe_user(age =11,color='light white'),u3.greet_user()
print()