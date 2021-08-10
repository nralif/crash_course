#10.12

import json

def check_stroage():
    filename = '../text_folder/favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except Exception as e:
        print(e)
    else:
        return number
def new_fav_num():
    fav_num = int(input('enter num: '))
    filename = '../text_folder/favorite_number.json'
    with open(filename,'a') as f_obj:
        json.dump(fav_num,f_obj)
    return fav_num

def display_fav_num():
    fav_num = check_stroage()
    if fav_num:
        print(f"your favorite number: {fav_num}")
    else:
        fav_num = new_fav_num()
        print(f'your fav num is {fav_num}')


display_fav_num()