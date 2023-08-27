from functools import lru_cache
import time
#normal
@lru_cache(maxsize=3)#the size is that how many timesleep you can use for using lru_cache'''''')"""this function is used when u want to print the next statements together witout any timesleep"""
def some_work(n):
    time.sleep(n)
    return n
print ("working")
some_work(3)
#some_work(2)
print("done...")
some_work(3)
print("calling again")