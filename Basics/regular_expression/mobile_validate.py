import re
n =input("Enter number:")
x = '[+][9][1][0-9]{10}'
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("not valid")
