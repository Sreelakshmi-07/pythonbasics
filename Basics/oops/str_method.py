class Student:
    clg_name = "Luminar"
    def __init__(self,name,roll,dept):
        self.name = name
        self.roll = roll
        self.dept = dept
    def printVal(self):
        print(self.name,self.roll,self.dept,Student.clg_name)
    def __str__(self):
        return self.name+"\t"+self.dept+"\t"+str(self.roll)           #string concat to get two values,covert to str to get int value
st = Student("anu",1,"cse")
st2 = Student("amal",2,"cse")
st.printVal()
print("Reference id(object related value[__str__])",st,st2)

