import re
s = input("Enter string:")
x = '^[A-Z][0-9]{5}'
match = re.fullmatch(x, s)
if match is not None:
    print("Valid")
else:
    print("Invalid")

#start with one capital letter
# exact 5 numbers