employees=[
    [1000,"ram","developer",25000,2],
    [1001,"abi","developer",35000,3],
    [1002,"anu","qa",45000,5],
    [1003,"kishan","qa",35000,3],
    [1004,"rahul","ba",28000,2]
    ,[1005,"tisa","devops",29000,2],
    [1006,"kiran","devops",30000,2]]
# ]
# # for i in employees:
# #     print([i[1]])
# #     if i[2] == "developer":
# #         print(i)
# # name = [emp[1] for emp in employees]
# # print(name)
# # print()
# names=list(map(lambda  emp:emp[1],employees))
# print(names)
# print()
# # dev = [emp[1] for emp in employees if emp[2] == "developer"]
# # print(dev)
# # print()
# devs=list(filter(lambda exp:exp[2]=="developer",employees))
# # print(devs)
# # print()
# print(list(map(lambda exp:exp[1],devs)))
# print()
# sal = [emp for emp in employees if emp[3]>25000]
# print(sal)
# print()
# sals=list(filter(lambda emp:emp[3]>25000 and emp[2]=="developer",employees))
# print(sals)
# print()
# print(list(map(lambda emp:emp,sals)))

employees.sort(key=lambda emp:emp[3],reverse=True)
print(employees)
print()
employees.sort(key=lambda emp:emp[4],reverse=True)
print(employees)
print(max(employees, key=lambda emp:emp[3]))
print(min(employees,key=lambda emp:emp[3]))