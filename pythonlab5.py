def age(dob):
    try:
        if (len(dob)==10):
            dob3 = dob.split("/")[2]
            print("your age is :", 2023-(int(dob3) ))
        else:
            raise Exception("you have entered invalid date format")

    except ValueError:
        print("warning !!"
            "please enter the date")

while(True):
        try:
            dob_str = input("Enter your date of birth (dd/mm/yyyy): ")
            if not dob_str:
                raise ValueError("please enter date incorrect format:")
                break
            elif dob_str=="?":
                print("please enter the date in this format :dd/mm/yyyy")
                continue
            elif dob_str=="q" or dob_str=="Q":
                print("Bye !!hope you run this program again")
                break
            age(dob_str)
        except ValueError:
                print("warning !!"
                "please enter the date")


else:
                raise Exception("Sorry, you have not entered in correct form")