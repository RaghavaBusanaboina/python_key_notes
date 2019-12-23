
'''
Variables  : STATE
Functions  : BEHAVIOR 

Entity 

Employee : eid name salary address company designation  # STATE
           get_emp_details()  R  # BEHAVIOR  
           update_emp_hike()  U
           save_emp_deatils() C 
           del_emp_details()  D

Web applications : DATA



expressoin equation 
2x2+3x+4   2x2+3x+4 = 0     



variables  x = 10
parameters   def func(x,y)
arguments    func(10,20)
fields       class object

declaration      int x;
intialization    int x = 10;
'''
x = 10+20

class int:
    def __init__(self,arg):
        self.arg = arg


class Employee:
    # STATE
    # constructor
    def __init__(self, eid, name, sal):
        self.eid = eid              # eid == local variable
        self.name = name            # self.eid = instance variable
        self.sal = sal

    # BEHAVIOR
    def get_emp_details(self): # instance method
        print("--- In Employee details screeen --- ")
        print("--Emp details are :", self.eid, " ", self.name, " ", self.sal)

# x = 10.5 str list tuple dict set 
madhu = Employee(100, "Madhu N", 1000)  # object creation
print(type(madhu))

madhu.get_emp_details()
Employee.get_emp_details(madhu)


mohan = Employee(101,"Mohan Co",2000)
mohan.get_emp_details()



print("***********************************************")
