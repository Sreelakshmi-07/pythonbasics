i = 1
f = 10
sum = 0
for i in range(i, f+1):
    if i % 2 == 0:
        sum = sum + i
print(sum)
print()
# while loop
initial = int(input("Enter initial number: "))
final = int(input("Enter final number:"))
sum = 0
while initial <= final:
    if initial % 2 == 0:
        sum = sum + initial
    initial = initial + 1
print(sum)
