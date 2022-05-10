# multilevel inheritance/hierarchical
class A:    #parent clss
    def printA(self):
        print("inside of A")
class B(A):     #parent class and child class
    def printB(self):
        print("inside of B")
class C(B):#child class
    def printC(self):
        print("inside of C")
d = C()
d.printA()
d.printB()
d.printC()
