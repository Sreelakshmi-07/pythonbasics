# regular expression
# to validate
# basic rules
# quantifiers(to extend basic)
# package re
# re used for pattern matching
# two methods fullmatch() and finditer()
import re
count =0
matche=re.finditer('ab',"abbbbababaaabba")
# for i in matche:
#     count = count+ 1
# print(count)
for i in matche:
    print(i.start())
    print(i.group())
    count = count + 1
print(count)