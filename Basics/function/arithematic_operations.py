# def main(num):
#         if num == 1:
#             return "Sum of ",a+b
#         elif num == 2:
#             return "Sub of: ", a-b
#         elif num == 3:
#             return "Div of:",a/b
#         elif num == 4:
#             return "multi of: ", a*b
#         elif num == 5:
#             break
#         else:
#             return "invalid"
# num = int(input("Enter number: "))
# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))
# print(main(num))
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x , y):
    return x/y
print("Operation\n1.add\n2.sub\n3.mul\n4.div\n5.stop")
while True:
    operation = int(input("Enter operation: "))
    if operation == 5:
        break
    else:
        n1 = int(input("Enter number: "))
        n2 = int(input("Enter number: "))
        if operation == 1:
            print(add(n1, n2))
        elif operation == 2:
            print(sub(n1, n2))
        elif operation == 3:
            print(mul(n1, n2))
        elif operation == 4:
            print(div(n1,n2))
        else:
            print("Invalid")

