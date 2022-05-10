def swap():
    num1 = int(input("Enter: "))
    n2 = int(input("Enter 2nd num: "))
    n3 = num1
    num1 = n2
    n2 = n3
    print(num1,n2)
swap()

def swap2(a, b):
    a, b = b, a
    print(a, b)
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
swap2(a, b)

def swap4(c,d):
    c, d = d, c
    return "After Swapping", c, d
print(swap4(9,5))