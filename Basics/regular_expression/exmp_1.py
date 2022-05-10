import re
s = input("Enter string:")
x = '^a[\w\W]*b$'
match = re.fullmatch(x, s)
if match is not None:
    print("valid")
else:
    print("invalid")