#10.5

filename = '../text_folder/programming_reason.txt'
with open(filename,'w') as file:
    while True:
        ask = input('enter why you like programming?\n ')
        if ask in ('q','Q','quit'):
            break
        else:
            print(f'Your say: {ask}')
        file.write(f"{ask}\n")