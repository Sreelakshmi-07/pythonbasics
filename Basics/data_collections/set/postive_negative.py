a = {1, 2, 3, 4, -1, 5, -3, -7, -9, 100}
positive_set = set()
negative_set = set()
for i in a:
    if i > 0:
        positive_set.add(i)
    else:
        negative_set.add(i)
print(positive_set)
print(negative_set)
