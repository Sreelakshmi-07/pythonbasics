import re
s = input("Enter string:")
x = '^A[\w\W]{3,8}B$'
match = re.fullmatch(x, s)
if match is not None:
    print("valid")
else:
    print("invalid")