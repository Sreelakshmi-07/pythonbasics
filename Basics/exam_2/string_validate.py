import re
string_one = input("Enter string:")
x = '[A-Za-z]'
match = re.fullmatch(x,string_one)
if match is not None:
    print("valid")
else:
    print("invalid")