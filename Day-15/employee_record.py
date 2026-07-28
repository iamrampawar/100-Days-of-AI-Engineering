# Employee Record Manager

employees = {
    1: {
        "name": "Rohan",
        "department": "HR",
        "salary": 35000
    },
    2: {
        "name": "Sneha",
        "department": "IT",
        "salary": 50000
    }
}

print("Employee Records")
print("-" * 30)

for emp_id, details in employees.items():
    print(f"Employee ID : {emp_id}")
    print(f"Name        : {details['name']}")
    print(f"Department  : {details['department']}")
    print(f"Salary      : ₹{details['salary']}")
    print("-" * 30)

# Update salary
employees[2]["salary"] = 55000

print("\nUpdated Salary of Sneha:")
print(employees[2])