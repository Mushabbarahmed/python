class student:
    no=9
    def __init__(self,aname,astd):
        self.name=aname
        self.std=astd
    def printdetail(self):
        return("assalamualikum")
    @classmethod
    def change(cls,no1):
        cls.no=no1
mub=student("hashim",1)
mub1=student("hashim1",11)
print(mub.name)
print(mub.printdetail())
mub.change(10)
mub.no=1
print(mub.no)
print(mub1.no)
