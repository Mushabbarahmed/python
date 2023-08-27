x=201
def harry():

    x=2

    def rohan():
        global x
    def rohan1():
        global x

        print("rohan =",x+1)
    print("before calling rohan()",x)
    rohan()
    rohan1()
    print("after calling rohan()", x)
def x1():
    global x
    return(x)
print(x1())
harry()
# print(x)
# x=200



# class f:
#     def __init__(self):
#         global x
#         #self.x=0
#         print(self.x)
#
# r1=f()
# print(r1.x)