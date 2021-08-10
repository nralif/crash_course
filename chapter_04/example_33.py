##4.11
pizza_lst = ['fpizza','spizza','tpizza']
friend_pizzas=[]
pizza_lst.append('npizza')
friend_pizzas.append('firstpizza')
count = 1
print('my fevarite pizza is:')
for i in pizza_lst:
    print(f'{count}: {i}')
    count+=1
count= 1
print('my friends pizza are: ')
for i in friend_pizzas:
    print(f'{count}: {i}')
    count+=1