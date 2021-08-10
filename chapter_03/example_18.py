#3.7


inviting_name = ['alif','rahman','rahim','karim']

print(f'* Hi {inviting_name[0]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[2]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[3]}. you are invited today in dinner.')

denie_name = 'karim'
rm_lst =inviting_name.remove(denie_name)
print()
print(inviting_name)
print()
print('new invite acceted people')
print()
print(f'* Hi {inviting_name[0]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[2]}. you are invited today in dinner.')

new_guest = inviting_name.insert(0,'abdullha')
new_guest2 = inviting_name.insert(2,'hasan')
new_guest3 = inviting_name.append('shaown')
print()
print(inviting_name)
print()

print(f'* Hi {inviting_name[0]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[2]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[3]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[4]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[5]}. you are invited today in dinner.')

warn_msg = 'you can invite only two people at this time.'
print(warn_msg)

print()
p1=inviting_name.pop(5)
p2=inviting_name.pop(4)
p3=inviting_name.pop(3)
p4=inviting_name.pop(0)
print(f'sorry {p1} we can\'t invite you at this time')
print(f'sorry {p2} we can\'t invite you at this time')
print(f'sorry {p3} we can\'t invite you at this time')
print(f'sorry {p4} we can\'t invite you at this time')
print()
print(inviting_name)
print()
print(f'* Hi {inviting_name[0]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.')

del inviting_name[0]
del inviting_name[-1]
print(inviting_name)


#