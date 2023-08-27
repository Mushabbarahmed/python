from datetime import datetime
import time

from pygame import mixer

class student:
    var=19
    no_of_leave = 9
    def __init__(self,aname,aroll,aclass):
        self.name=aname
        self.std=aclass
        self.roll=aroll
    def printdetails(self):
        return print ("student name is",self.name,"and class is",self.std,"and roll number is",self.roll)
    #class method process for this we have to use "@classmethod"
    @classmethod
    def change_leave(cls,newleaves):
        cls.no_of_leave=newleaves
    #for class method as alternative method
    @classmethod
    def change_dash(cls,st):
        #param=st.split("-")
        #return cls(param[0] , param[1] , param[2])
        #or(option
        return cls(*st.split("-"))
    @staticmethod
    def printgood(st,gt):
        print ("this is good  "  , st , str([str(datetime.now())] ) ,gt)
#inheritance process begins from here (this is single inheritance) meaning inheriting the other class
class programmer(student):
    def __init__(self,aname,aroll,aclass,aprogram):
        self.name = aname
        self.std = aclass
        self.roll = aroll
        self.prog=aprogram
    def printprog(self):
        return f"student name is{self.name}and class is{self.std} and roll number is{self.roll} and langauges are{self.prog}"
class player:
    var=10
#multipleinheritance
class coolprogrammer(student,player):
    var=20
    language="html"
    def print_prog(self):
        print(self.language)
mub=student("mubashir",3,1)
hashim=student("hashim",2,1)
mub.printdetails()
# humaid=student.change_dash("humaid-1-2")
# print(mub.std)
# print(humaid.std)
# print(student.no_of_leave)
# hashim.no_of_leave=10
# hashim.change_leave(30)
# print(student.no_of_leave)
# print(hashim.no_of_leave)
mub.printgood("brother",str([str(datetime.now())]))
print(datetime.now())
humaid=programmer("humaid",2,1,["cpp","python"])
# print(humaid.printprog())
# print(humaid.no_of_leave)
# #humaid.change_leave(10)
# print(student.no_of_leave)
# print(humaid.no_of_leave)
# mub.change_leave(1)
# print(student.no_of_leave)
# #humaid.change_leave(12)
# print(student.no_of_leave)
# print(humaid.no_of_leave)
ham=coolprogrammer("hammad",1,2)
ham.printdetails()
print(ham.var)
ham.print_prog()
print(humaid.var)
humaid=coolprogrammer("humaid",2,1)
humaid.print_prog()
print(datetime.now())
print(time.time())
print(datetime.now())
# i=0
# while i<5:
#     mixer.init()
#     mixer.music.load("E:\songs\water.mp3")
#     mixer,music.play()
#     a=input("type")
#     if a==1:
#         mixer.music.stop()
#         break
#     i=i+1
def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
#             break
# music("E:\songs\water.mp3","stop")
#mixer.init()
#mixer.load("E:\songs\water.mp3")
#mixer.play()