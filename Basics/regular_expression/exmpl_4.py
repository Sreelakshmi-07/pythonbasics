import re
s = input("Enter string:")
x = '^5[0-9\W]+'
match = re.fullmatch(x, s)
if match is not None:
    print("valid")
else:
    print("invalid")