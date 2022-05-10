# Ascending pattern
# for i in range(5): # i = 0,1,2,3,4
#     for j in range(i):
#         print("*", end=" ")
#     print()
# Descending pattern
for i in range(5, 0, -1):
    for j in range(i - 1):
        print("*", end=" ")
    print()
