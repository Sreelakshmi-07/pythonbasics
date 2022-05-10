class School:
    def __init__(self,schoolname,schoolid):
        self.schoolname = schoolname
        self.schoolid = schoolid
class Classes(School):
    def __init__(self,class_no,dept):
        self.class_no = class_no
        self.dept = dept
class Student(Classes,School):
    def __init__(self,schoolname,schoolid,class_no,dept,student_no,marks,avg):
        self.student_no = student_no
        self.marks = marks
        self.avg = avg
        School.__init__(self,schoolname,schoolid)
        Classes.__init__(self,class_no,dept)
    def printl(self):
        print(self.schoolname,self.schoolid,self.class_no,self.dept,self.student_no,self.marks,self.avg)
stu = Student("Snvb",1001,101,"Commerce",1,95,"86%")
stu.printl()



