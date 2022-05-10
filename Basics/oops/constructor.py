# constructor
class Person:
    def __init__(self,name,age1):
        self.name = name
        self.age = age1
    def Printvalue(self):
        print(self.name)
        print(self.age)
pe = Person("anu", 25)
pe.Printvalue()
pe1 = Person("amal", 25)
pe1.Printvalue()
