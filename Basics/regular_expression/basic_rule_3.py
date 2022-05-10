import re
x = '[^a-z]'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '[a-z]'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '[0-9]'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '[^a-zA-Z0-9]'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '\d'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '\w'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '\W'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())
print()
x = '\D'
match = re.finditer(x,"hello a123@bc AC")
for i in match:
    print(i.group())