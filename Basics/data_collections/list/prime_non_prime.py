list1 = [4, 7, 9, 2, 11, 67, 87, 34, 23, 12, 98, 54, 33]
prime = list()
non_prime = list()
for i in list1:
    if i > 1:
        i += 1
        for j in range(2,i):
            if i % j == 0:
             non_prime.append(j)
            else:
                 prime.append(j)
print(non_prime)
print(prime)

