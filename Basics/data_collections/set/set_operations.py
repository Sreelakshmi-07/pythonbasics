# union
# intersection
# difference
set1 = {1, 2 , 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1, "-set1 \n", set2, "-set2")
set3 = set1.union(set2)
print(set3, "-union")
set4 = set1.difference(set2)
print(set4, "-difference")
set5 = set1.intersection(set2)
print(set5, "-intersection")