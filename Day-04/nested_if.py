age = int(input("Enter your age:"))
citizens = input("Are you indian citizen?(Yes/No)")

if age>=18:
    if citizens == "Yes":
        print("You are eligible to vote")
    else:
        print("You are not eligible because you are not an indian citizen")
else:
    print("You are not eligible because you are under 18")

