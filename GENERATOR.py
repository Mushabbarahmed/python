#GENERATOR IIS USED TO CREATE YOUR OWN ITERTOR FUNCTION LIKE FOR LOOP IN GENERATOR YIELD IS USED INSTEAD OF RETURN
# this one is for loop (normal)
def gen( n):
    for i in range(0,n):
        return i
# this is genrator if  used(YIELD)
def gen2():
    yield "a"
    yield "i"
def gen1(n):
    for i in range(n):
        yield i#ACTS LIKE RETURN

g=gen(3)
print(g)
g2=gen2()
print(g2.__next__())
g1=gen1(3)
print(g1.__next__())
print(g1.__next__())#this next function is used to display one element one after the other till where user wants
print(g1.__next__())
#print(g1.__next__())

# For string  we have to use (ITER)funtion for making it generator
h="hahsim"
i=iter(h)
print(i.__next__())#note: iter function cannot be used for (INT) BUT IF WE USED IT IN TUPLE WAY WE CAN USE INT ALSO AND EVEN IN LIST WE CAN ITERATE
print(i.__next__())
print(i.__next__())
for i in gen2():
    print(i)