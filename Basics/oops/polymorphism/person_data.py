class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printVal(self):
        print(self.name,self.age)
f = open("person.txt","r")
for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    age = data[1]
    p = Person(name,age)
    p.printVal()
