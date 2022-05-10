class Bank:
    bname = "SBI"
    def acc_create(self,acc,name):
        self.acc = acc
        self.name = name
        self.minbal = 5500
        self.balance = self.minbal
    def deposit(self,amt):
        self.amt = amt
        self.balance = self.balance + self.amt
        print("your",Bank.bname,"Total amount credited",self.amt,"balance",self.balance)
    def withdraw(self,withdrawn):
        self.withdrawn = withdrawn
        if self.withdrawn>self.balance:
            print("No minimum balance")
        else:
            self.balance = self.balance - self.withdrawn
            print("Your",Bank.bname,"debited with",self.withdrawn)
            print("your balance",self.balance)
user1 = Bank()
user1.acc_create("anu",1234)
a = int(input("Cash to deposit"))
user1.deposit(a)
b = int(input("Cash to withdraw"))
user1.withdraw(b)

