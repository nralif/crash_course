#6.5

revers = {
    'padma':'bangladesh',
    'nile':'egypt',
    'bramuprotro':'chin',
    'barmuda':'usa',
    'gongga':'india'
}

for i in revers:
    print(f'the {i} runs through {revers[i]}.')
    print()

print('revers in dictionary:')
for i in revers:
    print(f'rever name: {i.capitalize()} ====>> country name: {revers[i].capitalize()}')

