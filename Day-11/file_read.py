print("===== Reading a File =====")

file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()