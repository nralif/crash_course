#7.10
users = {}

active = True
while active:
    name = input('enter your name:')
    place = input("If you could visit one place in the world, where would you go?")
    users[name] =place

    people = input("Do you want to add person: 'y/n'")
    if people in ('n','no','nop','nope'):
        active = False
for user,places in users.items():
    print(f"Hi {user}.")
    print(f"you want to visite {users[user]}\n")
