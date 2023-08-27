l1=["humaid","hashim","hassan","hammad"]
i = 1
for  item in l1:
    if i % 2 != 0:
        print(item)
    i=i+1
print(end=" \n")
for index,item in enumerate(l1):
    if index%2==0:
        print(item)
