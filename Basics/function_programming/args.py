def sum(*args):
    # return args
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum(3,4,2,1))     #output in tuple format
