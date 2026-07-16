age = int(input("Enter Your age:"))
citizen = input("Are you indian?:(Yes/No)")

if age>=18 and citizen == "Yes":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote.")