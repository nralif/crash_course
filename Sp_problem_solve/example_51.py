#
prime =[]
not_prime =[]
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            not_prime.append(i)
            break

    else:
        prime.append(i)
print(f'Prime Number: {prime}')
print(f'Not Prime Number: {not_prime}')