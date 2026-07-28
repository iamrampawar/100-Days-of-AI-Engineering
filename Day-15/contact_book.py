# Contact Book

contacts = {
    "Rahul": "9876543210",
    "Priya": "9123456780",
    "Amit": "9988776655"
}

print("Contact Book")
print("-" * 30)

for name, number in contacts.items():
    print(f"{name} : {number}")

search = "Priya"

if search in contacts:
    print(f"\nPhone Number of {search}: {contacts[search]}")
else:
    print("Contact not found.")
    