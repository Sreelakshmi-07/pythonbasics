min = int(input("Enter range:"))
max = int(input("Enter range:"))
for i in range(min,max):
    if i % 2 == 0:
        for a in range(5,0,-1):
            for j in range(a):
                print(i,end=" ")
            print()
    else:
        for a in range(5):
            for j in range(a):
                print(i,end=" ")
            print()