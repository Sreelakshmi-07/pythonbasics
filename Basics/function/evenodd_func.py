# without args
def evenodd():
    a = int(input("Enter number: "))
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
evenodd()

# with args
def evenodd2(b):
    if b % 2 == 0:
        print("Even")
    else:
        print("odd")
b = int(input("Enter number:"))
evenodd2(b)

# with return type
def evenodd3(c):
    if c % 2 == 0:
        return "even"
    else:
        return "odd"
    return c
c = int(input("Enter number: "))
print(evenodd3(c))