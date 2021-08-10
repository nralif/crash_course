##5.8

reg_name = ['admin','alif','karim','rahim','rahman','abdul']
user_input =str(input('enter your user name: '))

if user_input in reg_name:
    if user_input == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'hello, {user_input}. thank you for loggin.')
else:
    print('please chack enter user name.')