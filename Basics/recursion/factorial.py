# recursion
# main exmp fibonacci,factorial

# n = int(input("Enter number:"))
# f = 1
# for i in range(1,n+1):
#     f = i * f
# print(n,"=",f)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))