s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 66, 33}
odd_set = set()
even_set = set()
for i in s:
    if i % 2 == 0:
        even_set.add(i)
    else:
        odd_set.add(i)
print(odd_set)
print(even_set)
