#6.7

users = {
    'alif':{
        'fname':'alif',
        'lname':'hasan',
        'address':'dhaka'
    },
    'naeem':{
        'fname':'naeemur',
        'lname':'rahman',
        'address':'Kishoregonj',
    },
}
check_lst =['naeem']

for user,user_info in users.items():
    for i in check_lst:
        if i in user:
            if user in users.keys():
                print(f'\nUser Name: {user}')
                print(f"\tFull Name: {user_info['fname']} {user_info['lname']},\n\tLocation: {user_info['address']}")
            else:
                print('something is wrong.')

