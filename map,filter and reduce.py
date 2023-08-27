# map process
#this is for adding list if numbers are given as strings and convert string into integer
# numbers=["3","34","64"]
# for i in range(len(numbers)):#len is used because len= will provide length of list as [0,1,2]
#     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])
# #or this is used for adding list directly
# n=[1,4,2]
# add=n[0]+n[2]
# #print(add)
# n1=["34","36","45","46"]
# n1=list(map(float,n1))
# n3=n1[0]+4.4
# print(n3)

def sq1(a):
     return a*a
# # def sq2(b):
# #     return b*b
# # def fun(x,y):
# #     return x[0],y[1]
num=["2","34","5"]
num11=("2","34","5")
num1=tuple(map(int,num11))#map is used for ieteration in one line
print(num1)
square=tuple(map(sq1,num1))
print(square)
# # #filter process-used to use funtion and on which u want to apply as well as iteration
# # list1=[1,2,3,4,5]
# # n1=list(map(sq1,list1))
# # print(n1)
def greater5(num):
    if num>5:
         print(num)

l1=[1,2,3,4,56,7,8,8,9]
n=list(filter(greater5,l1))
print(n)
# #reduce process
# # first we have to import reduce
# from functools import reduce
# list1=[1,2,3,4,5]
# num=reduce(lambda x,i:x+i,list1)
# print(num)
# num1=list(map(sq1,list1))
# print(num1)


