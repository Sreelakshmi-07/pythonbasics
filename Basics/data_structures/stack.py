# LIFO
# push pop
global list1

list1 = []
size = int(input("Enter size:"))
top = 0
def push():
    global size
    global top
    if top >= size:
        print("Stack is full")
    else:
        e = int(input("Add elements"))
        list1.append(e)
        top = top + 1
        print(list1)
def pop():
    global size
    global top
    if top <= 0:
        print("Stack is empty")
    else:
        list1.pop()
        top = top - 1
        print(list1)
while True:
    choice = int(input("Enter choice \n 1.Push \n 2.Pop \n"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    else:
        print("Invalid input")



