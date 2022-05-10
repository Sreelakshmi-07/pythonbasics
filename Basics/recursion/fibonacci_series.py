# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))

# n terms
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1)+fibonacci(n - 2)
nterms = 10
for i in range(nterms):
    print(fibonacci(i))
