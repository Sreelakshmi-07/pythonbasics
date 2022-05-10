initial = int(input("Enter initial range:"))
final = int(input("Enter final range:"))
for i in range(initial , final +1):
    for j in range(initial, i):
        print(j, end= ' ')

    print()