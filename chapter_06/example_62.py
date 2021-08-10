#6.10

fav_num ={
    'alif': [5,29],
    'rahim':[23,543],
    'karim':[24,54],
    'masud':[87],
    'abdul':[76,32]
}
for name,num in fav_num.items():
    print(f"\nName: {name}")
    print('your number are:')
    for n in num:
        print(f'{n}')
