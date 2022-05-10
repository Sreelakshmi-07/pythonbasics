l1 = [1, 6, 8, 9, 2, 3, 4]
# inbuilt method l.sort()
l2 = list()
while l1:
    mini = l1[0]
    for i in l1:  #i,1
        if i < mini:  # 1 < 6
            mini = i
    l2.append(mini)
    l1.remove(mini)
print(l2)