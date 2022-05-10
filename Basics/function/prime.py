# 2,3,5,7,..
num =int(input("Enter number: "))
if num > 0:
    for i in range(2,num):
        if num % i == 0:
            print(num, "not prime")
            break
    else:
        print(num, "prime")
