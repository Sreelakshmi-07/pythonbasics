import re
f = open("ex.txt","r")
f2 = open("e.txt","w")
x ='[L][U][M]\d{2}[P][Y]\d{2}'
for i in f:
    data = i.rstrip("\n")
    match = re.fullmatch(x,data)
    if match is not None:
        f2.write(data)
        f2.write("\n")


