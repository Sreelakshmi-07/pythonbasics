f = open('data.txt', 'r')
f1 = open('copy.txt', 'a')
f1.write("\n")
for i in f:
    f1.write(i)
