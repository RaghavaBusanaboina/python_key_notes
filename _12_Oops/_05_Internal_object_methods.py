
import string

class Employee(object):
    # FIELDS 
    # para constructor
    '''
    test
        eid
        eid name
        eid sal
        eid name sal

    '''
    def __init__(self, eid , name = "MadhuNettem", sal = 10000):
        self.eid = eid
        self.name = name
        self.sal = sal

    # METHODS
    # INSTANCE METHOD
    def get_emp_hike(self,sal = 1000):
        print("----In get employee hike----------")
        
    # INSTANCE METHOD
    def get_emp_desn(self,hike):
        if(self.sal <= 100000):
            print(self.name, " is a softwatre trainee")
        else:
            print(self.name, " is a softwatre engineer")   
            
            
madhu = Employee(100,"MadhuN")   
madhu.get_emp_desn(100)
madhu.get_emp_hike(100000)  
   
          
# Built in class attributes '''
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)

# Functions   C R U D
print("Has salary : ", hasattr(madhu, "sal"))
print("Set name   : ",setattr(madhu, "name", "MAD")) 
print("Get name   : ",getattr(madhu, "name"))
print("Del salary : ",delattr(madhu, "sal")) 
# print("Get salary : ",getattr(madhu, "sal"))
