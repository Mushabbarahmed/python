class student:
    def __init__(self,aname,aroll,aclass):
        self.name=aname
        self.std=aclass
        self.roll=aroll
    def printdetails(self):
        return print ("student name is",self.name,"and class is",self.std,"and roll number is",self.roll)
mub=student("mubashir",3,1)
#mub.name="mubashir"
#mub.std=9
(mub.printdetails())
print(mub.std)