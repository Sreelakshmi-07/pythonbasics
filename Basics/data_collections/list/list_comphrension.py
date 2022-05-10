a = [1, 2, 3, 4]
sq = [i * i for i in a]
print(sq)
# for i in a:
#     i = i * i
#     sq.append(i)
# print(sq)
l = [1, 2, 1, 2, 1, 2, 1, 2, 2, 1]
newlist = [i for i in l if i == 2]
print(newlist)

nl = [i for i in range(1, 20+1) if i % 2 == 0]
print(nl)
