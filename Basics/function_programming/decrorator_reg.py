import re
def mailvalidate(func):
    def wrapper(m,p):
        x = '[\w\W]+[@][a-zA-Z]+[.][a-z]{2,3}'
        match = re.fullmatch(x,m)
        if match is not None:
            return func(m,p)
        else:
            raise Exception("Mail not valid")
    return wrapper
@mailvalidate
def login(mail,password):
    print("logged in")
mail = input("Enter email:")
password = int(input("Enter password"))
login(mail,password)