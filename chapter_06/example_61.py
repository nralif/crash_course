# 6.9

favorite_places = {
    'naeem':{
        'first':'dhaka',
        'second':'kishoregonj',
        'third':'chittagonj'
    },
    'alif':{
        'first':'norsindi',
        'second':'manikgonj',
        'third':'mymansing'
    },
    'rahman':{
        'first':'rangpur',
        'second':'gazipur',
        'third':'kustia'
    }
}
ask_info =['alif','rahman']
for name,place in favorite_places.items():
    # for names in ask_info:
    if name in ask_info:
        print(f'Hi {name}. thanks for share your info.')
        while True:
            confirm = input("do you want to add some place: 'y/n'")
            if confirm.lower() in ('y','yes','yeap','yeah','ye','yeo'):
                s_place = int(input('how many fav place do you want to share with us:\n'))
                p = []
                if s_place>0:
                    while s_place+1>1:
                        places = input('enter your places: ')
                        p.append(places)
                        s_place-=1
                    print(p)
                    break
                elif s_place < 0:
                    print('please enter correct place.')
                    continue
                elif s_place in (00, 000, 0000, 00000):
                    print('thanks.But you are not share your info.')
                    print('your previous places:')
                    if name in favorite_places.keys():
                        print(f"\n\tFirst place: {place['first'].capitalize()},\n\tSecond Place: {place['second'].capitalize()}\n\tThird Place:{place['third'].capitalize()}")
                        break
                else:
                    print('something is wrong.')
                    break
            elif confirm.lower() in ('n','no','nop','nope'):
                print("you are enter 'no'.so i think....")
                print('your are not interested to share additional place.')
                print('Here your previous places:')
                if name in favorite_places.keys():
                    print(f"\n\tFirst place: {place['first'].capitalize()},\n\tSecond Place: {place['second'].capitalize()}\n\tThird Place:{place['third'].capitalize()}")
                    break
            else:
                print('enter a wrong input')
    else:
        print(f'Hi,{name}.')
        print('yor fav places:')
        if name in favorite_places.keys():
            print(f"\n\tFirst place: {place['first']},\n\tSecond Place: {place['second']}\n\tThird Place:{place['third']}")
        else:
            print('please here some problem')