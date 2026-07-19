cart = []

print("Shopping Cart Program :")

item1 = input("Enter first item :")
item2 = input("Enter second item :")
item3 = input("Enter third item :")

cart.append(item1)
cart.append(item2)
cart.append(item3)

print("\n Shopping Cart :")

print(cart)



remove_item = input("\n Enter an item to remove: ")

if remove_item in cart:
    cart.remove(remove_item)
    print("Item remove successfully!")

else:
    print("Item not found\n ")

print("Update Cart :")
print(cart)


print("\n Total Items :",len(cart))
