# a = input("Enter string: ")
# e = 'a'
# count = 0
# for i in a:
#     if i in e:
#         count = count + 1
# print(count)
# another method
a = input("Enter string: ")
e = 'a'
count = 0
for i in a:
    if i == 'a':
        count = count + 1
print(count)
# count
a = input("Enter string: ")
e = a.count('a')
