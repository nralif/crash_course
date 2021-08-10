#

file_name = '../text_folder/pi_digits.txt'
with open(file_name) as file:
    lines = file.readlines()

pi_string =''
for line in lines:
    pi_string+=line.strip()

birthday = input('enter your birthday,format "yymmdd: "')
if birthday in pi_string:
    print('birthday is appear')
else:
    print('not appear')
print(pi_string[:52]+'...')
print(len(pi_string))