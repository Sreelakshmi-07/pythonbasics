class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printVal(self):
        print(self.name,self.age)
class Child:
    def __init__(self,phn):
        self.phn = phn
class Student(Person,Child):
    def __init__(self,rollno,dep,name,age,phn):
        # super().__init__(name,age) for only one super class
        Person.__init__(self,name,age)
        Child.__init__(self,phn)
        self.rollno = rollno
        self.dep = dep
    def prinl(self):
        print(self.name,self.age,self.rollno,self.dep,self.phn)
st = Student(1,"cse","arun",21,89898989)
st.prinl()
