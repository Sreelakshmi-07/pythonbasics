# # set method
# a = "abcd"
# c = "cdef"
# a = set(a)
# c = set(c)
# if a & c:
#     print(a & c)
# else:
#     print("not elements")

a = "abcd"
c = "cdef"
for i in a:
    if i in c:
        print(i)
