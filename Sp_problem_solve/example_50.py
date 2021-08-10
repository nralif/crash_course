
a =0
b =1
lst =[]
while a<=100:
    lst.append(a)
    c =a+b
    a = b
    b = c
print(lst)
print()

x = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(x)):
    print(f'{i+1}: {x[i]}')