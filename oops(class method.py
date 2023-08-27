from datetime import datetime
class student:
    no_of_leave = 9
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
    def add( x1, b):
        ad = x1 + b
        print(ad)
    @staticmethod#thi ssttic metho dis used when u eant to agive argument to add in this class function without self
    def printgood(st):
        print ("this is good  "  , st , str([str(datetime.now())] ))

mub=student("mubashir",3,1)
hashim=student("hashim",2,1)
#mub.printdetails()
#print(mub.no_of_leave())
humaid=student.change_dash("humaid-1-2")
# print(mub.std)
print(humaid.std)
(humaid.add(2,1))
# print(student.no_of_leave)
# hashim.no_of_leave=10
# hashim.change_leave(30)
# print(student.no_of_leave)
# print(hashim.no_of_leave)
mub.printgood("brother" )

#print(datetime.now())