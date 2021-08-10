#10.7

while True:
    try:
        f_num = input('enter a num: ')
        if f_num in ('q','Q','quit'):
            break
        l_num = input('enter a num: ')
        if l_num in ('q','Q','quit'):
            break
        sum = int(f_num)+int(l_num)
    except TypeError:
        continue
    except ValueError:
        continue
    else:
        print(sum)