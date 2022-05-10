def usercheck(func):
    def wrapper(v1,v2):
        if v1 == "admin":
            return func(v1,v2)
        else:
            raise Exception("not allowed")
    return wrapper
@usercheck
def changepin(user,pin):
    mypin = pin
    return mypin
# print(changepin("user1",123))
print(changepin("admin",134))