l1 = [1, 4, 22, 55, 88, 11, 100,47, 50]
l2 = list()
while l1:
    mini = l1[0]
    for i in l1:  #i,1
        if i < mini:  # 1 < 6
            mini = i
    l2.append(mini)
    l1.remove(mini)
else: print("maximum",l2[-1])
print("minimum",l2[0])
print(l2)