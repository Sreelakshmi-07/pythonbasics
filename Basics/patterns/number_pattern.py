# num = 0
# for i in range(5):
#     for j in range(i):
#         num += 1
#         print(num,end= " ")
#     print()

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
        j += i
    print()
# Another method
# for i in range(5):
#     num = 1
#     for j in range(i):
#         print(num,end= " ")
#         num += 1
#     print()