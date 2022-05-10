name = input("Enter string: ")
vowels = 'aeiou'
a = ""
for i in name:
    if i not in vowels:
        a += i
print(a)