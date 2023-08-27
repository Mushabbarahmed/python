class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}{lname}@gmail.com"
    def explain(self):
        return f"the employee is {self.fname} {self.lname}"
    @property#property decorator is used if user dont want to use function with"()"
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set"
        return f"{self.fname}{self.lname}@gmail.com"

        pass
    @email.setter
    def email(self,str):
        name=str.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
mub=employee("mubashir","ahmed")
print(mub.email)
mub.fname="humaid"
print(mub.email)
mub.email="this.that@gmail.com"
print(mub.email)
del mub.email
print(mub.email)