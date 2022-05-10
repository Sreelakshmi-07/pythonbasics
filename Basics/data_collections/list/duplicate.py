l = [1, 2, 3, 4, 5, 6, 1, 2, 3]
b = list()
c = list()
for i in l:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print(c)
