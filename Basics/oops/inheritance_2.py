# person name,age
# student name age rollno dept
class Person:
    def persona(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def stud(self,rollno,dept):
        self.rollno = rollno
        self.dept = dept
        print("Student \n",self.name,self.age,self.rollno,self.dept)
class Employee(Person):
    def emp(self,id,dep,salary):
        self.id = id
        self.dep = dep
        self.salary = salary
        print("Employee:",self.id,self.name,self.age,self.dep,self.salary)
stu = Student()
empl = Employee()
stu.persona("Aji",22)
stu.stud(1001,"comp")
empl.persona("Anju",30)
empl.emp(101,"Comp",25000)
