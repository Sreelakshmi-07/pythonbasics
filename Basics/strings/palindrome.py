s = input("Enter string: ")
a = ""
for i in s:
    a = i + a
if s == a:
    print("Palindrome")
else:
    print("Not palindrome")
print()
# Another method
j = input("Enter string: ")
rev = j[::-1]
if j == rev:
    print("Palindrome")
else:
    print("Not palindrome")
