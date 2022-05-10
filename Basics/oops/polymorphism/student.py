class Student:
    def __init__(self,name,rollno,dept):
        self.name = name
        self.rollno = rollno
        self.dept = dept
    def printVal(self):
        print(self.name,self.rollno,self.dept)
f = open("stu.txt","r")
for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    rollno = data[1]
    dept = data[2]
    st = Student(name,rollno,dept)
    st.printVal()