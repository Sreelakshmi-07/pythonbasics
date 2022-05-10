class Employee:
    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept = dept
    def printVal(self):
        print(self.name,self.id,self.dept)
    def __str__(self):
        return self.name+"\t"+str(self.id)
emp = Employee("Amal",1001,"acc")
print(emp)