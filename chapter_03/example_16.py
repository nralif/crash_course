#3.5

inviting_name = ['alif','rahman','rahim','karim']

print(f'* Hi {inviting_name[0]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[1]},{inviting_name[3]} and {inviting_name[2]}')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[2]},{inviting_name[3]} and {inviting_name[0]}')
print(f'* Hi {inviting_name[2]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[0]},{inviting_name[3]} and {inviting_name[1]}')
print(f'* Hi {inviting_name[3]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[0]},{inviting_name[2]} and {inviting_name[1]}')

denie_name = 'karim'
ni_lst =inviting_name.remove(denie_name)
print()
print('new invite acceted people')
print()
print(f'* Hi {inviting_name[0]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[1]} and {inviting_name[2]}')
print(f'* Hi {inviting_name[1]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[2]} and {inviting_name[0]}')
print(f'* Hi {inviting_name[2]}. you are invited today in dinner.'
      f'\t please come cause also come {inviting_name[0]} and {inviting_name[1]}')




#