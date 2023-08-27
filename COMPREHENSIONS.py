#LIST COMPREHENSIVE
#string="Asasasassaasasasaas"
ls=[i for i in range(10)]
print(ls)# through list comprehensive we can write for loop in one line
# #dictionary using list comprehensive
dict1={i:f"item is {i}" for i in range(5)}
print(dict1)
# #we can even revesre dictinary
# dict2={value:key for key,value in dict1.items()}
# print(dict2)
dress={ dress for dress in ["dress1","dress2","dress1","dress3","dress2"]}#this used to print the sets only once the repeated one will be rejected"
print(dress)
# print(type(dress))
# dress1=[ dress for dress in ["dress1","dress2","dress3","dress1","dress2"]]
# print(dress1)
# print(type(dress1))
even=(i for i in range(100) if i%2==0)#for using comprehensive using generator then we have to use parenthesis()
print(even.__next__())
# print(even.__next__())
# #simple for loop it iterates automatically
# #for items in even:
#  #   print(items)

















