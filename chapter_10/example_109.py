#10.11
import json
fav_num  = int(input('enter number: '))

filename = '../text_folder/favorite_number.json'
with open(filename,'w') as file:
    json.dump(fav_num,file)

with open(filename) as file:
    number =json.load(file)
    print(f"i know your fav num is {number}")