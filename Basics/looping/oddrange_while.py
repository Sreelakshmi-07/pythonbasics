initial = int(input("Enter initial range: "))
final = int(input("Enter final range: "))
while initial <= final:
    if initial % 2 != 0:
        print(initial)
    initial += 1
