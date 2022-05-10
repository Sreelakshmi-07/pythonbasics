class Student:
    def __init__(self,name,rollno,dept):
        self.name = name
        self.rollno = rollno
        self.dept = dept
    def Printvalue(self):
        print(self.name,self.rollno,self.dept)
s = Student("anju",101,"comp")
s.Printvalue()