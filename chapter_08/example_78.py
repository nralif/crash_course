#8.5

def describe_city(city='Dhaka',country='Bangladesh'):
    n=3
    des = {}
    while n > 0:
        city = input('enter city: ')
        country = input('enter country:')
        des[city] = country
        n -= 1
    for city, country in des.items():
        print(f'{city} is in {des[city]}.')

describe_city()