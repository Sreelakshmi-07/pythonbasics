# def sub(n1,n2):
#     print(n1-n2)
# sub(4,7)
# decorators can be used multiple times
def changevalue(func):
    def wrapper(a,b):
        if a > b:
            return func(a,b)
        else:
            a,b=b,a
            return func(a,b)
    return wrapper
@changevalue
def sub(n1,n2):
    print(n1-n2)
sub(1,7)
sub(7,1)
