# 9.5
class User:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.login_attempts =0

    def describe_user(self,**others_info):
        information = {}
        for name, info in others_info.items():
            information[name] = info
        print('your info:')
        print(f"\tFull Name: {self.fname} {self.lname}")
        for name,value in information.items():
            print(f"\t{name}: {value}")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hi {self.fname}. Have a nice day.")

u= User('alif','hasan')
u.increment_login_attempts()
print(u.login_attempts)
u.reset_login_attempts()
print(u.login_attempts)