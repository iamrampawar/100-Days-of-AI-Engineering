def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiiply(a,b):
    return a*b

def division(a,b):
    if b== 0:
       return "Division by 0 is not allowed"
    return a/b

num1 = float(input("Enter a number:"))
num2 = float(input("Enter a number:"))

print("\n Choose Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your choice(1-4):")

if choice == "1":
    print("Result:",add(num1,num2))

elif choice == "2":
    print("Result:",subtract(num1,num2))

elif choice == "3":
    print("Result :",multiiply(num1,num2))

elif choice == "4":
    print("Result:", division(num1,num2))


else: 
    print("Invalid choice!")
    


