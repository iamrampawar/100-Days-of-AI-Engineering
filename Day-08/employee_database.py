print("==== Employee Database =====")

employee = {}

employee["id"] = input("Employee Employee ID:")
employee["name"] = input("Enter Employee name:")
employee["department"] = input("Enter department:")
employee["salary"] = float(input("Enter Salary :"))

print("\n Employee Details")

for key,value in employee.items():
    print(f"{key.capitalize()} :{value}")

print("\nUpdating Salary..")
employee["salary"] += 5000

print("\n After salary Update")
for key,value in employee.items():
   print(f"{key.capitalize()}:{value}")

remove = input("\n Do you want to remove Dapartment?(yes/no) :")

if remove.lower == "yes":
    employee.pop("department")

print("\n final employee record")

for key,value in employee.items():
   print(f"{key.capitalize()} : {value}")