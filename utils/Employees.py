

class Employees:

    class Employee:
        def __init__(self,eid,name,designation,salary,x):
            self.eid=eid
            self.name=name
            self.designation=designation
            self.salary=salary
            self.x=x

    employeesDetails=[]
    
    def addEmployee(self,eid,name,designation,salary,x):
        self.employeesDetails.append(self.Employee(eid,name,designation,salary,x))
    
    def allEmployeeSalaryTotal(self):
        totalSalary=0
        for i in self.employeesDetails:
            totalSalary+=i.salary
        return totalSalary
    
    def totalEmployee(self):
        return len(self.employeesDetails)
    
    def printAllEmployeeDatails(self):
        # print("Eid  Name  designation   salary   Details")
        for i in self.employeesDetails:
            print(i.eid,i.name,i.designation,i.salary,i.x)
            

ee=Employees()
ee.addEmployee(1,"hb","H",20000,"SomeDetails")

ee.addEmployee(2,"db","H",20000,"SomeDetails")
print(ee.totalEmployee())
print(ee.printAllEmployeeDatails())
print(ee.allEmployeeSalaryTotal())