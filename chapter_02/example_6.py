#split the msg

msg ='''Albert Einstein once said, “A person who never made a mistake never tried anything new.” '''

s=msg.split(',')
print(s[1])
a = s[0].split(' ')
print(f'{a[0]} {a[1]}')
#