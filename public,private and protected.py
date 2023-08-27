from datetime import datetime
class student:
    var=19
    no_of_leave = 9#this are all are public because it can access by any class instance
    #to use protected use ("__")
    _dance=5#this can be accesed by class and sub class memebrs
    #to use private us("__")befor any variable name
    __private=2#this can be accsed by only class members

    def __init__(self,aname,aroll,aclass):
        self.name=aname
        self.std=aclass
        self.roll=aroll
    def printdetails(self):
        return print ("student name is",self.name,"and class is",self.std,"and roll number is",self.roll)
    #class method process for this we have to use "@classmethod"
    @classmethod
    def change_leave(cls,newleaves):
        cls.no_of_leave=newleaves
    #for class method as alternative method
    @classmethod
    def change_dash(cls,st):
        #param=st.split("-")
        #return cls(param[0] , param[1] , param[2])
        #or(option
        return cls(*st.split("-"))
    @staticmethod
    def printgood(st,gt):
        print ("this is good  "  , st , str([str(datetime.now())] ) ,gt)
#inheritance process begins from here (this is single inheritance) meaning inheriting the other class
class programmer(student):
    def __init__(self,aname,aroll,aclass,aprogram):
        self.name = aname
        self.std = aclass
        self.roll = aroll
        self.prog=aprogram
    def printprog(self):
        return f"student name is{self.name}and class is{self.std} and roll number is{self.roll} and langauges are{self.prog}"
class player:
    var=11
class p1(student):
    var=2
    pass
#multipleinheritance
class coolprogrammer(student,player):
    var=20
    language="html"
    def print_prog(self):
        print(self.language)
mub=student("mubashir",3,1)
print(mub._dance)
hu=programmer("humaid",10,2,2)
ha=p1("hashim",1,2)

ham=coolprogrammer("hammad",1,1)
print(ham.var)
print(ha.name)
print(mub._student__private)#to acces this type as typed
print(ha.name)
# hashim=student("hashim",2,1)
# mub.printdetails()
# humaid=student.change_dash("humaid-1-2")
# print(mub.std)
# print(humaid.std)
# print(student.no_of_leave)
# hashim.no_of_leave=10
# hashim.change_leave(30)
# print(student.no_of_leave)
# print(hashim.no_of_leave)
# print(mub._dance)
# mub.printgood("brother",str([str(datetime.now())]))
# print(datetime.now())
# humaid=programmer("humaid",2,1,["cpp","python"])
# print(humaid.printprog())
# print(humaid.no_of_leave)
# #humaid.change_leave(10)
# print(student.no_of_leave)
# print(humaid.no_of_leave)
# mub.change_leave(1)
# print(student.no_of_leave)
# #humaid.change_leave(12)
# print(student.no_of_leave)
# print(humaid.no_of_leave)
# ham=coolprogrammer("hammad",1,2)
# ham.printdetails()
# print(ham.var)
# ham.print_prog()
# print(humaid.var)
# humaid=coolprogrammer("humaid",2,1)
# humaid.print_prog()
# print(datetime.now())
# print(time.time())
# print(datetime.now())
print(ha._dance)