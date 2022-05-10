num = int(input("enter num : "))
def fact(num):
    f = 1
    i = 1
    while i <= num:
        f = f * i
        i = i + 1
    return f
print(fact(num))