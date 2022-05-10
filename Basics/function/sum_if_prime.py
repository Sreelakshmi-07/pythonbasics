initial = 1
final = 10
sum = 0
for num in range(initial, final+1):
    if num > 0:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                sum = sum + num
print(sum)