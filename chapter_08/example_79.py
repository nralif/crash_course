#8.6

def city_country(city='dhaka',country='bangladesh'):
    num =0
    city_info = {}
    while num<3:
        city = input('enter city name: ')
        country = input('enter country name:')
        city_info[city] =country
        num+=1
    for city,country in city_info.items():
        print(f"\"{city},{city_info[city]}\"")

city_country()