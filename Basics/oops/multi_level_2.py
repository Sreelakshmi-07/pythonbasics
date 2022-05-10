class Parent:
    def parentA(self,name,age):
        self.name = name
        self.age = age
class Child(Parent):
    def childA(self,relation):
        self.relation = relation
class Student(Child):
    def stud(self,rollno,school):
        self.rollno = rollno
        self.school = school
        print("Parent-",self.name,self.age,"Child-",self.relation,self.rollno,self.school)
d = Student()
d.parentA("Anju",25)
d.childA("Daughter")
d.stud(1001,"Snvb")