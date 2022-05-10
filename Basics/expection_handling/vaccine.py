age = int(input("Enter age:"))
if age >= 18:
    print("Eligible for vaccination")
else:
    raise Exception("Not eligible")
