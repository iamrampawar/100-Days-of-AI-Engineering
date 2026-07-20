print("====Student Management System====")

student = {}

student["name"] = input("Enter student name :")
student["age"]  = int(input("Enter student age :"))
student["branch"] = input("Enter student branch :")
student["CGPA"] = float(input("Enter student CGPA:"))

print("\n----student Details----")
for key,value in student.items():
    print(f"{key.capitalize()} : {value}")

print("\nDictionary keys :",student.keys())
print("Dictionary values :", student.values())
