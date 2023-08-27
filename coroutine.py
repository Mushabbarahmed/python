import time
def search():
    import time
    book="hashim is a good boy and he is studying in 8th std"
    time.sleep(4)
    while True:
        text=(yield)
        if text in book:
            print("text is in book")
        else:
            print("text is not in book")

time.sleep(2)
s1=search()
print("start searhing."".")
next(s1)#this is important to start the function while using coroutine method
s1.send("hashim")#then to send values use this line
input("press any key")
s1.send("has")
input("press any key")
s1.send("bad")
