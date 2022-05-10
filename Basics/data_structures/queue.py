# Queue
# FILO
# enqueue dequeue
global list1

list1 = []
size = int(input("Enter size:"))
front = 0
def enqueue():
    global size
    global front
    if front >= size:
        print("Queue is full")
    else:
        e = int(input("Add elements"))
        list1.append(e)
        front= front + 1
        print(list1)
def dequeue():
    global size
    global front
    if front <= 0:
        print("Queue is empty")
    else:
        list1.remove(list1[0])
        front = front - 1
        print(list1)
while True:
    choice = int(input("Enter choice \n 1.Enqueue \n 2.Dequeue \n"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    else:
        print("Invalid input")