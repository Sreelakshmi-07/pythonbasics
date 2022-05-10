num = int(input("enter number: "))
def find_posneg(num):
    if num == 0:
        print("zero")
    elif num > 0:
        print("Positive number")
    else:
        print("Negative number")
find_posneg(num)