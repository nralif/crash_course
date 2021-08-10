#8.4
def make_shirt(size='L',msg = 'i love pyhton'):
    if size in ('L','M','l','m'):
        print('i love pyhton')
    elif size in ('s','S','XL','xl','XXL','xxl','xxxL','XXXL'):
        print(msg)
    else:
        print('enter correct info.')
make_shirt('l','this is not medium or large size shirt.')
