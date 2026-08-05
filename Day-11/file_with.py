print("===== Using with Statement =====")

with open("student.txt", "r") as file:
    content = file.read()

print(content)