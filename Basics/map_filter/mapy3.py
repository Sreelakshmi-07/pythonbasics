lis=[2,3,4,6,7,8,9]
def list1(num):
    if num < 5:
        return num - 1
    else:
        return num + 2
out=list(map(list1,lis))
print(out)