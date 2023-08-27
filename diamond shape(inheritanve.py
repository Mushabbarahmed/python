class A:
    def met(self):
        return "inside class a constructor"
class B(A):
    def met(self):
        return "inside class b constructor"
class C(A):
    #def met(self):
        #return "inside class c constructor"
        pass
class D(C,B):
    def met(self):
        return "inside class d constructor"
    pass
# a=A()
# b=B()
c=C()
#d=D()
print(c.met())


