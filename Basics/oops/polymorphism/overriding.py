# same method same num of args
class A:
    def printData(self,num):
        self.num = num
        print("Inside A class",self.num)
class B(A):
    def printData(self,num2):
        self.num2 = num2
        print("inside B",self.num2)
b1 = B()
b1.printData(5)
# child class overrides parent class in same no of args