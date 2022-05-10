initial = int(input("Enter initial range:"))
final = int(input("Enter final range: "))
for i in range(initial, final+1): #num=1,2,3,4,5
    if i > 0:
        for j in range(2,i): #i=2,4,5
            if i % j == 0:
                break
        else:
             print(i)

# a = int(input("Enter initial range:"))
# b = int(input("Enter final range: "))
# for i in range(a, b+1):
#     if i > 1:
#         for j in range(2,i):
#             if i % j != 0:
#                 break
#         else:
#              print(i)
