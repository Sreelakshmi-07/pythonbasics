f = open("appending.txt",'r')
dict1 = {}
for i in f:
    data = i.rstrip("\n").split(" ")
    print(data)
    word_count = {}
    for word in data:
        if word not in word_count:
            word_count.update({word: 1})
        else:
            val = word_count[word]
            val += 1
            word_count.update({word: val})
    print(word_count)


