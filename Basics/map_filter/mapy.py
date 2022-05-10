list1=[10,11,12,13]
def square(num):
    return num**3
out=map(square,list1)
print(list(out))
squ=list(map(lambda num:num**2,list1))
print(squ)