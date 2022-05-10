# linear search
# l = input("Enter element")
# j = ["hello", "world"]
# # flag = 0
# for i in j:
#     if i == l:
#         # flag = 1
#         print("present")
#         break
# else:
#     print("not present")
# another method
def linear_search():
    l = input("Enter element")
    j = ["hello", "world"]
    flag = 0
    for i in j:
        if i == l:
            flag = 1
            break
    if flag == 1:
        print("present")
    else:
        print("not present")
linear_search()