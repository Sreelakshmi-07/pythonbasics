# print odd numbers from initial and final range
initial = int(input("Enter initial range: "))
final = int(input("Enter final range: "))
for initial in range(initial, final+1):
    if initial % 2 != 0:
        print(initial)