#8.10
def make_great(name):
    while name:
        current_name = name.pop()
        modify = f"{current_name} is a good magician."
        modify_name.append(modify)

def show_magicians(name,m):
    print("this are original name:")
    for user in name:
        print("\t",user)
    print('\nthis is modify names:\n')
    for modify in m:
        print(f"\t{modify}")

names =['alax','dickot','duplace','albrat']
modify_name =[]
make_great(names[:])
show_magicians(names[:],modify_name)
