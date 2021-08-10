#10.8

file1 = 'text_folder\cats.txt'
file2 = 'text_folder\dogs.txt'
try:
    with open(file1,'r') as f1:
        x=f1.readlines()
        for i in x:
            print(i.strip())
    print()
    with open(file2,'r') as f2:
        y=f2.readlines()
        for i in y:
            print(i.strip())
except FileNotFoundError:
    print('file is missing.')
except FileExistsError:
    print("file doesn't not exist")
else:
    pass