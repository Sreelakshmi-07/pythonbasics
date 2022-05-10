# s = input("Enter string: ")
# b = ""
# c = ""
# for i in s:
#     if i not in b:
#         b = b + i
#     else:
#         if i not in c:
#             c = c + i
# print(c)

s = input("Enter string: ")
b = ""
for i in s:
    if i not in b:
        b = b + i
print(b)



