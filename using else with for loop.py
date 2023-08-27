khana=["roti","parata","shawarma","pani puri"]
for item in khana:
    print(item)
else:
    print("for loop runned properly")

a=input("enter")
for item in khana:
    if item==a:
        print("found")
        break
else:
    print("item is not found")