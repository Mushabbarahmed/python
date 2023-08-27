# a=input("enter your name")
# b=input("enter")
#
# if a.isnumeric():
#     raise Exception("numbers are not allowed")
# if int(b)==0:
#     raise ZeroDivisionError("b is not ")
# print("hello",a)
c=input("enter")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise  ValueError("harr is blocked")
    print("handled")

