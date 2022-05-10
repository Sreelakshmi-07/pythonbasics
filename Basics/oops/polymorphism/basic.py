# polymorphism
# two concepts :- 1. method overload 2. method overriding
# method overloading not supported
class A:
    def printData(self,a):
        self.a = a
        print("inside",self.a)
class B(A):
    def printData(self,a,b):
        self.a = a
        self.b = b
        print(self.a,self.b)
b1 = B()
b1.printData(1,2)