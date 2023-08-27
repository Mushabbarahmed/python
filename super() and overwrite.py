class a:
    var1="hi in class A"
    classvar1="instance"
    def __init__(self):
        self.classvar1="inside class a constructor"
class b(a):
    var1="hi in class b"
    def __init__(self):#this process is called overwriting because it is inherited class a but printing the classvar1 from classs b only #if init was not written here then it would print he values of class a

        self.classvar1="inside class b constructor"
        super().__init__()#this is super funtion used here
        print(super().classvar1)
a=a()
b=b()
print(a.classvar1)
print(b.classvar1)
