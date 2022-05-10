import re
f = open("valid_num.txt","w")
x = '[+][9][1]\d{10}'
for i in range(5):
    num = input("Enter number:")
    match = re.fullmatch(x,num)
    if match is not None:
        f.write(num)
        f.write("\n")