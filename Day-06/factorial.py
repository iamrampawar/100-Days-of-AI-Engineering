# Day 6 Mini Project - Factorial Calculator

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


number = int(input("Enter a number: "))

print("Factorial of", number, "is", factorial(number))