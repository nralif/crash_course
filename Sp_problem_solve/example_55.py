#

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print([[row[i] for row in matrix] for i in range(4)])

add =[]
for k in range(4):
    trans_row = []
    for r in matrix:
        trans_row.append(r[k])
    add.append(trans_row)


print(add)
print(list(zip(*matrix)))
