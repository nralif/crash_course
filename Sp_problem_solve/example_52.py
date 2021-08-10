#

a=2
while a<100:
    b = 2
    while b<a:
        if a%b == 0:
            print(f'np:{a}\n',end=',')
            break
        b+=a
    else:
        print(f'p:{a}',end=',')
    a+=1

