import re
s = input("Enter string:")
x = '[A-Z\d]{3,7}'
match = re.fullmatch(x, s)
if match is not None:
    print("valid")
else:
    print("invalid")