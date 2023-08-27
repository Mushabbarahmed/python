class student:
    no_of_leave = 9
    def __init__(self,aname,aroll,aclass):
        self.name=aname
        self.std=aclass
        self.roll=aroll
    def printdetails(self):
        return print ("student name is",self.name,"and class is",self.std,"and roll number is",self.roll)

    @classmethod
    def change_leave(cls, newleaves):
        cls.no_of_leave = newleaves
    def __add__(self, other):#DUNDER METHOD
        return self.name+other.name
    def __truediv__(self, other):
        return self.std/self.std
    def __repr__(self):# used when when want to print details without using . opertaion
           return f"('{self.name}','{self.std}','{self.roll}')"
    def __str__(self):
        return f"thname is {self.name}"

s1=student("humaid",1,2)
s2=student("hashim",2,3 )
print(s1+s2)
print(s1/s2)
print(repr(s1))
print(str(s1))# FOR MORE METHODS LIKE ADD,TRUEDIV SEARCH IN FOR MAPPING OPERTAION IN FUNCTION IN GOOOGLE
