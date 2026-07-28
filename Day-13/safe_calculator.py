print("===== Safe Calculator =====")

try:
    # Take input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Choose operation
    operation = input("Choose operation (+, -, *, /): ")

    # Perform calculation
    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        result = num1 / num2

    else:
        result = None
        print("Invalid operation selected.")

# Handle invalid number input
except ValueError:
    print("Please enter valid numbers.")

# Handle division by zero
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Executes only if no exception occurs
else:
    if result is not None:
        print(f"\nResult = {result}")

# Always executes
finally:
    print("\nThank you for using Safe Calculator!")