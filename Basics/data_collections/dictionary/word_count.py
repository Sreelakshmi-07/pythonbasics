s = input("Enter String:")
a = s.split(" ")
print(a)
# hello:2 hi:1
word_count = {}
for i in a:
    if i not in word_count:
        word_count.update({i:1})
    else:
        val = word_count[i]
        val += 1
        word_count.update({i:val})
print(word_count)