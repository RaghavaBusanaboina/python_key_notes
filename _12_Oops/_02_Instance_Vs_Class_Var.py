
'''
#---------------------BEFORE----------------------
print("---------------------BEFORE----------------------")
class Employee:
    def __init__(self, eid, name, sal, office_name = "ORACLE"):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.office_name = office_name

    # METHODS
    def get_emp_hike(self):
        print("----In get employee hike----------")

    def get_emp_desn(self):
        if(self.sal <= 15000):
            print(self.name, " is a software trainee, office is :",self.office_name)
        else:
            print(self.name, " is a software engineer office is :",self.office_name)

madhu = Employee(100,"MadhuN",10000)  # Object creation, madhu is an object which is of type Employee
madhu.get_emp_desn()  # Employee.get_emp_desn(madhu)
 
mohan = Employee(200,"MohanG",25000)
mohan.get_emp_desn()

print("---------------------BEFORE----------------------")
'''


class Employee:
    # class variables
    office_name = "ORACLE"  # Class Variable  1. Sharable
    emp_count = 0           #                 2. Sharable + Modifiable

    # constructor   # instance variables
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # METHODS
    # INSTANCE METHOD
    def get_emp_hike(self):
        print("----In get employee hike----------")

    # INSTANCE METHOD
    def get_emp_desn(self):
        if(self.sal <= 15000):
            print(self.name, " is a softwatre trainee and his company name is ",Employee.office_name)
        else:
            print(self.name, " is a softwatre engineer and his company name is ",Employee.office_name)

'''
1. Class Defined and provided special method i.e, __init__(constructor) method to initialize instance variables, 
    define respective methods to get the BEHAVIOR
2.  Create object for the respective class.
        Internally 
         - Python creates empty object for us,and gives reference to "self" parameter
         - Reamaining parameters, we are passing as arguments
         - In empty object, instance variables will be initialized with the given data
3. Finally whole object reference will be given to LHS(object/instance,variable)
4. We can perform method calls using created object
'''

print("-----Empooyee count ---Company start-------",Employee.emp_count)

madhu = Employee(100,"MadhuN",10000)  # Object creation, madhu is an object which is of type Employee

print("-----Empooyee count --madhu--------",Employee.emp_count)
print(Employee.office_name)
print(madhu.get_emp_hike())
madhu.get_emp_desn()  # Employee.get_emp_desn(madhu)
 

mohan = Employee(200,"MohanG",25000)
print("-----Empooyee count ---mohan-------",Employee.emp_count)
mohan.get_emp_desn()