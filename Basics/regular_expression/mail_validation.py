import re
s = input("Enter email:")
x = '[a-zA-z0-9]+[@][A-Za-z]+[.]+[a-z]{2,3}'
match = re.fullmatch(x, s)
if match is not None:
    print("valid")
else:
    print("invalid")