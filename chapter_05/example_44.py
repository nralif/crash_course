##5.10

current_users = ['nralif','naeem','rahman','karim','rahim']
new_users = ['naeem','alif','RAHMAN','Rahman','karim','sajib']
for x in current_users:
    x.lower()
if current_users:
    for user in new_users:
            if user.lower() in current_users:
                print(f'{user} is already used.\n enter a new user name.')
            else:
                print(f'* {user} username is available.')
else:
    print('we need some user')

