# mark = int(input("Enter mark of subject: "))
# if mark > 100:
#     print("error")
# elif mark >= 90:
#     print("A+")
# elif mark >= 80:
#     print("A")
# elif mark >= 70:
#     print("B+")
# elif mark >= 60:
#     print("C")
# elif mark >= 50:
#     print("D")
# else:
#     print("Fail")
def grade(mark):
    if mark > 100:
        return "error"
    elif mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B+"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "Fail"
mark = int(input("Enter mark of subject: "))
print(grade(mark))