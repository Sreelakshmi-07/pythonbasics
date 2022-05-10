num = 10
a = 0
b = 1
for i in range(2, num):
    c = a + b
    a = b
    b = c
print(c)
print()
# Another method
n1 = 0
n2 = 1
cnt = 0
while cnt < 10:
    print(n1)  #0,1,1
    nth = n1 + n2  #1,2,3
    n1 = n2  #n1 = 1,2
    n2 = nth  #n2 = 1,2,3
    cnt += 1  #1,2
