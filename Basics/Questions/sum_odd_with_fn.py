def sumodd(a,b):
    s = 0
    for i in range(a,b+1):
        if i % 2 != 0:
           s = s + i
    return s
print(sumodd(40,80))

