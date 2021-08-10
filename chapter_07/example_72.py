#7.9
sandwich_orders =['fsand','pastrami','ssand','pastrami','tsand','pastrami']

finished_sandwich =[]
print('the deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

else:
    for i in sandwich_orders:
        finished_sandwich.append(i)
print(finished_sandwich)


