#8.8

def make_ablum(art_name='alif',art_album='bastobota'):
    art_info ={}
    take_info = 3
    while take_info>0:
        art_name = input('enter name:')
        if art_name in ('q','Q','QUIT','quit'):
            break
        art_album =input('enter album name: ')
        if art_album in ('q','Q','QUIT','quit'):
            break
        while art_album in art_info.values():
            print("you can't enter others album.\nplease enter your album name.")
            art_name = input('enter name:')
            art_album = input('enter album name: ')
            while art_album not in art_info.values():
                break
            continue
        else:
            art_info[art_name] =art_album
            take_info-=1
    for art_name in art_info.keys():
        print(f"\nhi {art_name},\n\tyour album is {art_info[art_name]}")

make_ablum()