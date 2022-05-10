class Person:
    def persona(self,name,age):
        self.name = name
        self.age = age
class Parent:
    def parenta(self,phn,address):
        self.phn = phn
        self.address = address
class Employee(Person,Parent):
    def emp(self,id,design,salary):
        self.id = id
        self.design = design
        self.salary = salary
        print(self.id,self.name,self.age,self.phn,self.address,self.design,self.salary)
e = Employee()
e.persona("anju",22)
e.parenta(9082938291,"ABC")
e.emp(1001,"accountant",25000)