#8.12
def make_sandwich(*items):

    print('add items on sandwich: ')
    for item in items:
        print(f'- adding {item}')
    print('making complete your sandwich.')
    print()


make_sandwich('chees','butter','panir','sos')
make_sandwich('panir','masala','sos','bread')
make_sandwich('sos','chees','bread','masala')