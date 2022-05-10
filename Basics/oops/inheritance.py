# inheritance
class A:
    def printa(self,nu):
        self.nu = nu
        print("Inside printa",self.nu)
class B(A):
    def printb(self,num):
        self.num = num
        print("inside printb",self.num)
        print(self.nu)
a = A()
a.printa(1)
b = B()
b.printa(5)
b.printb(2)
