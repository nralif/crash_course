#10.6

try:
    f_num = input('enter your num: ')
    l_num = input('enter your num: ')
    sum = int(f_num)+int(l_num)
except ValueError:
    print('please enter correct value.')
else:
    print(sum)
