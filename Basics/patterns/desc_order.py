for row in range(0, 5):
    for i in range(0, 5 - row - 1):
        print(" ", end=" ")
    for i in range(0, row + 1):
        print("*", end=" ")
    print(" ")
