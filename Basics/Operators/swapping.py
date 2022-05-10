a = 3
print("***Before Swapping***")
print(a)
b = 7
print(b)
c = a
a = b
b = c
print("***After Swapping***")
print(a)
print(b)
print()
# Another method which is only supported in python
num1 = 4
num2 = 5
print("Before Swapping \n num1: ",num1,"num2: ",num2)
num1, num2 = num2, num1
print("After Swapping \n num1: ",num1,"num2: ",num2)
# Method Three
n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("After swapping num1:", n1)
print("After Swapping num2: ", n2)