#
import json

def get_stored_username():
    filename = '../text_folder/username.json'
    try:
        with open(filename) as f_obj:
            username =json.load(f_obj)
    except FileExistsError:
        return None
    except Exception as e:
        print(e)
    else:
        return username
def get_new_user():
    filename  = '../text_folder/username.json'
    username = input('what is your name? ')
    with open(filename,'w') as file:
        json.dump(f"{username}",file)
    return username

def greating_user():
    verify_user = input('enter user name: ')
    username = get_stored_username()
    try:
        while verify_user in username:
            print(f"welcome back, {username}!")
            break
        else:
            username = get_new_user()
            print(f"We'll remember you when you come back, {username}!")
    except Exception as e:
        print(e)

greating_user()
