##5.7

favorite_fruits = ['banana','mango','waterlemon','dragon','lichi']
guess = str(input('enter your fruit :'))

if guess in favorite_fruits:
    print(f"you really like {guess}")
else:
    print(f'{guess} is wrong guess ')
