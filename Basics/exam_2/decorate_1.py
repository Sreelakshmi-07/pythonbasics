import re
def checkmail(func):
    def wrapper(v1,v2):
        if v1 == mailid:
            return func(v1,v2)
        else:
            raise Exception("not allowed")
    return wrapper
@checkmail
def login(mailid,password):
    if match is not None:
        return "successfully completed login process"
    else:
        return "Invalid Mail"
mailid=input("Enter mail:")
x = '[a-zA-z0-9]+[@][A-Za-z]+[.]+[a-z]{2,3}'
match = re.fullmatch(x, mailid)
password=input("Enter password:")
print(login(mailid,password))