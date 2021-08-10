#10.3
filename = '../text_folder/guest.txt'

name = input('enter your name: ')
with open(filename,'a') as file:
    file.write(f'\n{name}')

with open(filename, 'r') as file:
    x =file.readlines()
    for f in x:
        print(f.strip())