print("====Student Record System ====")

name = input("Enter Student Name :")
branch = input("Enter student branch :")
cgpa = input("Enter Student CGPA :")

with open("student.txt","a") as file:
    file.write(f"Name : {name}\n")
    file.write(f"Branch : {branch}\n")
    file.write(f"CGPA : {cgpa}\n")

    file.write("------------------\n")

    print("\n Student record saved successfully !")