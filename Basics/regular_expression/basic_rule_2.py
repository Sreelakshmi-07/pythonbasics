import re
x = '[^abc]'
match = re.finditer(x,"hello a123@bc")
for i in match:
    print(i.start())
    print(i.group())