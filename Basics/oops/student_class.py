class Student:
    college_name = "Snigst"  #static variable for common variable
    def setvalue(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        # self.college_name = college_name
    def printvalue(self):
        print(self.name,self.roll_no,self.department,Student.college_name)
pe = Student()
pe.setvalue("Anji",1001,"CS")
pe.printvalue()
pe2 = Student()
pe2.setvalue("Aji",1002,"Mcom")
pe2.printvalue()
# two types of variable in oops
# instance variable ..related to method..access using self
# static variable ... related to class .. access using class name