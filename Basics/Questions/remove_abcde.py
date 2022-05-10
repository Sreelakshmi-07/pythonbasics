s = input("Enter string:")
n = ""
for i in s:
    if i not in "abcde":
        n = n + i
print(n)


