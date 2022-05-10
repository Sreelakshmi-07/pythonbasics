# s = input("Enter string:")
# a = ""
# for i in s:
#     if i not in '!@#$%^&*()<>?,./;:"[]\{}-=_+':
#         a += i
# print(a)

# i>="a" and i<="z" or i>="A" and i <= "Z":
# Another method
s = input("Enter string:")
a = ""
for i in s:
    if i.isalnum():
        a += i
print(a)