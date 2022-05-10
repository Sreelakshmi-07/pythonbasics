list = [ 2,4,6,1,3,5,7,0,8,9]
def binary_search():
    list.sort()
    e = int(input("Element to search:"))
    flag = 0
    low = 0
    upper = len(list) - 1
    while low <= upper:
        mid = low + upper // 2
        if e == list[mid]:
            flag = 1
            break
        elif e > list[mid]:
            low = mid + 1
        elif e < list[mid]:
            upper = mid - 1
    if flag == 1:
        print("Element found")
    else:
        print("Element not found")
binary_search()
