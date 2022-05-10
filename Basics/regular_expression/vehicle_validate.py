import re
s = input("Enter vehicle number:")
x = '[K][L]\s[0-9]{2}\s[A-Z]{1}\s[0-9]{4}'
match = re.fullmatch(x,s)
if match is not None:
    print("valid")
else:
    print("Not valid")