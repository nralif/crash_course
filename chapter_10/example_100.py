#
filename = r'../text_folder/learning_python.txt'
table = '''Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far'''
with open(filename,'w') as file:
    sepfile = table.split(' ')
    for text in sepfile:
        file.writelines(f"in python you can --{text}\n")

with open(filename,'r+') as read:
    r =read.readlines()
    for i in r:
        print(i.strip())
