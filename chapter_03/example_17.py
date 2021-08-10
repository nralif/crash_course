#3.6

inviting_name = ['alif','rahman','rahim','karim']

print(f'* Hi {inviting_name[0]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[2]}. you are invited today in dinner.')
print(f'* Hi {inviting_name[3]}. you are invited today in dinner.')

denie_name = 'karim'
rm_lst =inviting_name.remove(denie_name)
new_lst = inviting_name
print()
print(new_lst)
print()
print('new invite acceted people')
print()
print(f'* Hi {new_lst[0]}. you are invited today in dinner.')
print(f'* Hi {new_lst[1]}. you are invited today in dinner.')
print(f'* Hi {new_lst[2]}. you are invited today in dinner.')

new_guest = new_lst.insert(0,'abdullha')
new_guest2 = new_lst.insert(2,'hasan')
new_guest3 = new_lst.append('shaown')
print()
new_lst2 =new_lst
print(new_lst2)
print()

print(f'* Hi {new_lst2[0]}. you are invited today in dinner.')
print(f'* Hi {new_lst2[1]}. you are invited today in dinner.')
print(f'* Hi {new_lst2[2]}. you are invited today in dinner.')
print(f'* Hi {new_lst2[3]}. you are invited today in dinner.')
print(f'* Hi {new_lst2[4]}. you are invited today in dinner.')
print(f'* Hi {new_lst2[5]}. you are invited today in dinner.')


#