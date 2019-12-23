'''
http://www.python-course.eu/python3_inheritance.php
http://www.python-course.eu/inheritance_example.php
'''

class Student:
    
    def __init__(self,rno,name):
        self.rno = rno 
        self.name = name
        
    def get_details(self):
        print("In student get_class method")
    
mad = Student(10,"Madhu")
mad.get_details()


class Employee(object):

    def __init__(self, eid, name):
        self.eid = eid
        self.name = name

    def get_emp_details(self):
        print("In Super Class : get_emp_details()")
        # print("Employee details are ", self.eid, " ", self.name)

    def get_info(self):
        print("In Super class : get_info()")

"""    def __add__(self, param):
        print("-----------in sublcass Employee add method---------------")
        return self.eid + param.eid
"""
class SoftwareEmployee(Employee):   # IS - A

    def __init__(self, eid, name, sal):
        Employee.__init__(self, eid, name)   # super().__init__(self, fName, lName)
        self.sal = sal

    def get_sw_emp_details(self):
        print("-------In Sub Class : get_sw_emp_deetailsI()-------------")

    def get_emp_details(self):
        print("In Sub Class : get_emp_details()")
print("*******************************")
madhu = Employee(10,"MAdhuN")
madhu.get_emp_details()
madhu.get_info()
print("*******************************")
shashank = SoftwareEmployee(11,"Shashank",1000)
shashank.get_sw_emp_details()
shashank.get_info()
shashank.get_emp_details()
shashank.m3()

print("*******************************")



pavan = Employee(110, "Pavan Kumar Balla")

pavan.get_emp_details()

print("Object   content is ",pavan)
print("Object   content is ",pavan.__str__())
print("Damu ojbect ", pavan.__str__())
gopi = Employee(111,"Gopi")

# print("Adding 2 objects of employee ", pavan + gopi)    #damu.__add__(gopi)




madhu.get_emp_details()
print("*******************************")
print("Type ",type(madhu))




#MRO - Method Resolution order

class A:
    def m1(self):
        print("In A")
class B:
    def m1(self):
        print("In B")
class C(A,B):
    def m2(self): 
        print("In C")
        
c = C()
c.m1()


