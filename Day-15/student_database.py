# Student Database using Dictionary

students = {
    101: {
        "name": "Rahul",
        "age": 20,
        "course": "AI & ML"
    },
    102: {
        "name": "Priya",
        "age": 19,
        "course": "Data Science"
    }
}

print("Student Database\n")

for roll, details in students.items():
    print(f"Roll No: {roll}")
    print(f"Name    : {details['name']}")
    print(f"Age     : {details['age']}")
    print(f"Course  : {details['course']}")
    print("-" * 30)

# Add new student
students[103] = {
    "name": "Amit",
    "age": 21,
    "course": "Cyber Security"
}

print("\nNew student added successfully!")