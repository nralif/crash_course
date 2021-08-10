#8.14

def make_car(model_name,manufacturer,**others_info):
    car_info ={}
    car_info['model_name']=model_name
    car_info['manufacturer'] =manufacturer
    for key ,value in others_info.items():
        car_info[key] =value
    return car_info


car = make_car('marchidis','banch',color = 'deep blue',
               tow_package =True)

print(car)