#7.4
print('enter a series of pizza toppings .\nenter \'q\' to Quit.')

while True:
    pizza = input('enter: ')
    if pizza.lower() in ('q','qu','qui','quit','qit','qt'):
        break
    else:
        print(f'+ add pizza {pizza}')
