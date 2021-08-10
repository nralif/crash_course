#

def make_shirt(size='L',msg='i Love python.'):
        while True:
            if size == 'M' or size == 'L':
                print('i love python')

            elif size == 'S':
                print('i small love python')
            else:
                print('enter a correct t-shirt size. ')


print("enter size into 's, m ,l' . otherwise getting wrong.")
size = input("enter t-shirt size: ")
size.upper()

make_shirt(size,msg='i love python')#