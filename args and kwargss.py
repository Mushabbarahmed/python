def funargs(normal,*arg,**kwarg):
    print(normal)
    for item in arg:
        print(item)
    #for key,value in kwarg.items():
    for item1,key in kwarg.items():
        print(key,item1)
k=(1,"humaid","mubashir","ajju","hammad")
n="these are the names of the brother"
kw=[["humaid","hashim"],["hassan","hammad"]]
k1=dict(kw)
funargs(n,*k,**k1)
print(k[0])
