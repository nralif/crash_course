#
vec = [[1,2,3], [4,5,6], [7,8,9]]

print([n for e in vec for n in e])
out =[]
for elem in vec:
    for num in elem:
        out.append(num)
print(out)