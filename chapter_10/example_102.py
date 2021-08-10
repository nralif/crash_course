#10.4

filename = '../text_folder/guest_book.txt'
while True:
    name = input('enter your name: ')
    if name in ('q',"q","quit"):
        break
    else:
        pass
    with open(filename,'a') as file:
        file.write(f"{name}\n")
        print(f"Hi {name},have a nice day.")
