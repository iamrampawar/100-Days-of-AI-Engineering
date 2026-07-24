print("====Notes App====")

note = input("Enter your note :")

with open("note.txt " ,"a") as file:
    file.write(note + "\n")


print("\n Note saved successfully!")