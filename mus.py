import pandas
from pygame import mixer
# print("hello world")
# n=int(input("enter the number "))
# #0 1 1 2 3 5
# i=0
# def fib(n):
#     if(n==0):
#         return 0
#     if (n==1):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# while(i<=n):
#         i=i+1
#         print(fib(i))
def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break

music("E:\songs\water.mp3","stop")