f = open('exe.txt', 'r')
for i in f:
    print(i.rstrip("\n"))
# empty line is also printed
# to remove extra line use r.strip
