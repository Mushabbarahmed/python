from datetime import datetime
def func1(dec1):
    def num1():
        print("x is good boy")
        dec1()
        print("executed")
    return num1

def who():
    print("y is good boy")
# #to use decorator function use @func1-{this is function made}
@func1
def how():
    print("how are you ")
# who1=func1(how)
how()
# #func1()
# who1()
# # print(datetime.now())
# who1=func1(who)
# print(who1())