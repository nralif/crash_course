# 6.7

users = {
    'alif': {
        'fname': 'alif',
        'lname': 'hasan',
        'address': 'dhaka'
    },
    'naeem': {
        'fname': 'naeemur',
        'lname': 'rahman',
        'address': 'Kishoregonj',
    },
}
check_list =['alif','naeem']
for user,user_info in users.items():
    if user in check_list:
        print(f'Username: {user}')
        full_name =user_info['fname']+' '+user_info['lname']
        location =user_info['address']

        print(full_name.title())
        print(location.title())