def vaccine_check(func):
    def wrapper(a,b):
        if b >= 18:
            return func(a,b)
        else:
            raise Exception("Not allowed")
    return wrapper
@vaccine_check
def vaccine(name,age):
    print(name,"Vaccination successful")
vaccine("amal",19)
vaccine("anu",14)