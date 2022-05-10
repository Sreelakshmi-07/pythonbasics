# for i in 'luminar technolab':
#     if i == 'a':
#         continue
#     print(i)
# s = "Luminar technolab"
# b=""
# for i in s: #h,e,l...
#     if i == 'a':
#         continue
#     else:
#         b+=i # hel...
# print(b)
# another method
s = "Luminar technolab"
b=""
for i in s:
    if i not in "a":
        b += i
print(b)
