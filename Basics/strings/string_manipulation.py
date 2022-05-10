# string manipulation
s = "hello"
print(type(s))
# using for loop
st = "hello"
for i in st:
    print(i)
print()
# multi printing conditions
h = "hello"
e = input("Enter element")
flag = 0
for i in s:
    if i == e:
        flag = 1
        break
if flag == 1:
    print("present")
else:
    print("not present")

# method
k = "world"
j = input("Enter element: ")
for m in k:
    if m == j:
        print("present")
        break
else:
    print("not present")
print()
# membership method
cha = " Hello world"
fin = input("Enter string :")
if fin in cha:
    print("present")
else:
    print("not present")