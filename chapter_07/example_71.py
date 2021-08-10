#
sandwich_orders =['fsand','ssand','tsand']
finished_sandwiches=[]
while sandwich_orders:
    cooking_sandwich = sandwich_orders.pop()

    print(f"complete sandwich: {cooking_sandwich.title()}")
    finished_sandwiches.append(cooking_sandwich)

print('\nThe following sandwich are made:')
for finished in finished_sandwiches:
    print(finished.title())
