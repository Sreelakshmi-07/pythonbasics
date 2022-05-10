a = int(input("Enter number:"))
b = int(input("Enter number:"))

# try and except
try:
    c = a / b
    print(c)
except Exception as e:
    print(e)
finally:
    print("Works always")