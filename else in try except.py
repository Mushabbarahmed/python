

try:
    f=open("mub12.txt")
except EOFError as t:
    print("print eof error agaya",t)
except IOError as t:
    print("print io error agaya",t)

else:

    print("thi will run only if except is not running")
finally:
    print("run this anyway....")
print("important to print anyway")

print(1.0/"S")
a=[0,11,0b01]
print(a[5])