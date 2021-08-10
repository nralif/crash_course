#
import random
num = random.randint(1,100)


while True:
    try:
        u_ipt =int(input('enter a number between 1 to 100: '))
        if u_ipt >num:
            print('its too high.')
        elif u_ipt<num:
            print('its too low')
        else:
            print('it got the number.')
            print('thanks for play game')
            break
    except Exception as e:
        print('Please enter a number.')

#