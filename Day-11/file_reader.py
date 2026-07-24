print("===== File Reader =====")

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

except FileNotFoundError:
    print("File not found.")