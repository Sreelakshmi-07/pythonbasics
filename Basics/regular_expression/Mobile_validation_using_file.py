import re
f = open("mobile.txt","r")
x = '[+][9][1][0-9]{10}'
for i in f:
    number = i.rstrip("\n")
    match = re.fullmatch(x, number)
    if match is not None:
        print(number)



