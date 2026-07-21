print("====Unique Visitor Tracker ====")

visitors = set()

visitor1 = input("Enter visitor 1 :")
visitor2 = input("Enter visotor 2 :")
visitor3 = input("Enter visitor 3 :")
visitor4 = input("Enter visitor 4 :")

visitors.add(visitor1)
visitors.add(visitor2)
visitors.add(visitor3)
visitors.add(visitor4)

print("\n Union Visitors :",visitors)

print("\nTotal Unique Visitors :",len(visitors))


check_visitor = input("Enter visitor name to check :")

if check_visitor in visitors :
    print(check_visitor,"has already visited")
else:
    print(check_visitor,"is a new visitor")


print("===== Visitor Management System =====")

visitors = set()

while True:
    visitor = input("Enter visitor name: ")
    visitors.add(visitor)

    choice = input("Do you want to add another visitor? (yes/no): ")

    if choice.lower() == "no":
        break

print("\n===== Visitor List =====")
for visitor in visitors:
    print(visitor)

print("\nTotal Unique Visitors:", len(visitors))