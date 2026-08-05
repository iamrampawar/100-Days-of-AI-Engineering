print("===== Writing to a File =====")

file = open("student.txt", "w")

file.write("Name: Ram\n")
file.write("Branch: IT\n")
file.write("CGPA: 7.19\n")

file.close()

print("Data written successfully.")
