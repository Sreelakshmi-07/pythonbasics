class Employee:
    def details(self,name,id,dept,salary):
        self.name = name
        self.id = id
        self.dept = dept
        self.salary = salary
    # def print(self):
        print(self.name,self.id,self.dept,self.salary)
emp = Employee()
emp.details("Amal",101,"Accounting",25000)
# emp.print()