# Day 10 - **kwargs Example

def student_info(**details):
    print("Student Details")
    print("----------------")

    for key, value in details.items():
        print(f"{key.capitalize()} : {value}")


student_info(
    name="Ram",
    age=20,
    branch="Computer Engineering",
    cgpa=8.5
)