#6.6

fav_lang ={
    'alif':'pyhton',
    'rahman':'c',
    'admin':'encode',
    'karim':'c++',
    'sajib':'ruby',
    'kasem':'c#',
    'abul':'java',
    'zubair':'js'
}
names = ['alif','rahman','admin']
# n = input('enter your name: ')
for name in fav_lang:
    if name in names:
        print(f'Hi \"{name.title()}, thanks for taking poll.\nyour fav lang is {fav_lang[name].title()}\"')
        print()
    else:
        print(f'{name}, please take our poll! ')
        while True:
            ask =input('Do you want to take a pull. \'y/n\'? ')
            if ask.lower() in ('y','yes','yeah','ye','yep'):
                lang = input('enter you fav lang: ')
                print(f'Thanks {name}, for taking our poll.\nyour fav lang is {lang}')
                print()
                break
            if ask.lower() in ('n','no','nop','nope'):
                print(f'ok! {name}. thanks for conversation.')
                print()
                break
            else:
                print('you enter worng input plz correct it.')