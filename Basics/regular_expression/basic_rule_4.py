import re
x = 'a{2,4}'
match = re.finditer(x,"aaaa aaaaaaaaaaaa aa aaa bbb abab @123 ABCD")
for i in match:
    print(i.start())
    print(i.group())
print()
x = '^a'  #^a used to check starting with
match = re.finditer(x,"aaaa aaaaaaaaaaaa aa aaa bbb abab @123 ABCD")
for i in match:
    print(i.start())
    print(i.group())
print()
x = '^[^abc]'  #^a used to check starting with
match = re.finditer(x,"aaaa aaaaaaaaaaaa aa aaa bbb abab @123 ABCD")
for i in match:
    print(i.start())
    print(i.group())
print()
x = 'a$'  #^a used to check ending with
match = re.finditer(x,"aaaa aaaaaaaaaaaa aa aaa bbb abab @123 ABCDa")
for i in match:
    print(i.start())
    print(i.group())