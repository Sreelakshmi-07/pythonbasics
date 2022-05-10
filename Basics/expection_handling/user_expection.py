def sub(num1,num2):
    if num1 < num2:
        raise Exception("negative value")
    else:
        print(num1 - num2)
sub(2,6)
# to create exception use "raise exception"
