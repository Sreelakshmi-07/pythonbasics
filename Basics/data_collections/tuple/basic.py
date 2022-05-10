tup = (1, 2, 3, 4)  #denote
print(tup)
print(type(tup))
tup1 = 1, 2, 3, 4, 8, 2, 5
print(tup1)
tup2 = (1, 2, (1, 5))  #nesting
print(tup2)
tup3 = ("hello", 1, 9.8,1)  #heterogenous,duplication
print(tup3)
print(tup3[::-1])  #slicing,indexing
print(tup3[2])
tup4 = ()
print(tup4)
# immmutable
for i in tup3:
    print(i)

print()

employees = (("anu", 1, "developer", 50000),
             ("arun", 2, "developer", 46000),
             ("amal", 3, "developer", 30000))
for i in employees:
    if i[-1] > 45000:
        print(i)
        