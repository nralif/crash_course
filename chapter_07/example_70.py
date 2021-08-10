#
responses = {}

active = True

while active:
    name = input('enter name:')
    response = input('live in city: ')

    responses[name] = response
    repeat = input('want add a person: ')

    if repeat == 'no':
        active =False

print('\n-----poll result----')
for name, response in responses.items():
    print(f"{name} would you live in  {response} city.")