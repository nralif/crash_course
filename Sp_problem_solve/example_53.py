#
def ask(prompt,retries =4,reminder = 'please try again.'):
    while True:
        ok = input(prompt)
        if ok.lower() in ('y','ye','yes'):
            return True
        if ok.lower() in ('n','nop','no','none','nope'):
            return False
        retries -=1
        if retries<0:
            raise ValueError('Invalid user response.')
        print(reminder)
ask('OK to overwrite the file?')