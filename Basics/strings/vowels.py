# a = input("Enter element: ")
# b = 0
# for i in a:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         b = b + 1
# print(b)

# another method
a = input("Enter element: ")
c = 'aeiou'
b = 0
for i in a:
   if i in c:
        b = b + 1
print(b)