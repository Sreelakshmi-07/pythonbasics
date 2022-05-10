# n = 123
# rev = 0
# while n > 0:
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10
# print(rev)
# another method
num = 123
s = str(num)
rev = s[::-1]
a = int(rev)
print(a)
print(type(a))
