# multiple inheritance
class A:
    def printA(self):
        print("inside A")
class B:
    def printB(self):
        print("inside B")
class D:
    def printD(self):
        print("inside D")
class C(A,B,D):
    def printC(self):
        print("inside C")
e = C()
e.printA()
e.printB()
e.printD()
e.printC()