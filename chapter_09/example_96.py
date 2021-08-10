# 9.8
class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.login_attempts = 0

    def describe_user(self, **others_info):
        information = {}
        for name, info in others_info.items():
            information[name] = info
        print('your info:')
        print(f"\tFull Name: {self.fname} {self.lname}")
        for name, value in information.items():
            print(f"\t{name}: {value}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hi {self.fname}. Have a nice day.")


class Privileges():
    def __init__(self):
        self.privileges =["can add post", "can delete post", "can ban user", "can update post", 'can add user']


    print('Admin can do:')
    def show_privileges(self):
        for privil in self.privileges:
            print(f"\t-{privil}")


class Admin(User):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.privilege = Privileges()

a =Admin('naeemur', 'rahman')
a.privilege.show_privileges()
