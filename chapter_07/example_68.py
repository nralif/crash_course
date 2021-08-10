#7.5

# active = True
while True:
    age = int(input('enter your age: '))
    if age>0 and age<130:
        if age<3:
            print('Get a Free Ticket.')
        elif age>3 and age<12:
            print('the ticket is $10')
            break
        else:
            print('the ticket is $15')
            break

    else:
        print('please enter a positive number.\nor a correct value not over 130 year.')