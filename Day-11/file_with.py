print("==== Using With Statement ====")

with open("Student.txt","r") as file :
    
    content = file.read()

    print(content)