# Shopping Cart System

cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Shopping Cart")
print("-" * 30)

for item in cart:
    print(item)

cart.remove("Mouse")

print("\nAfter Removing Mouse")

for item in cart:
    print(item)