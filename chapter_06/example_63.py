#6.11

cities ={
    'dhaka':{
        'country':'Bangladesh',
        'population': 25000000,
        'fact':'over population'
    },
    'beijing':{
        'country':'china',
        'population':180000000,
        'fact':'populated because old history'
    },
    'darline':{
        'country':'germany',
        'population':7500000,
        'fact':'beautiful and well managed'
    }
}


for city,city_info in cities.items():
    if city in cities.keys():
        print(f'Here, {city.capitalize()} are all information :')
        for city in cities.keys():
            print(f"\tCountry: {city_info['country'].capitalize()}\n\tPopulation: {city_info['population']}\n\tFact: {city_info['fact'].capitalize()}\n")
            break