# Day 10 - *args Example

def calculate_sum(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total


print("Sum of 10 and 20 :", calculate_sum(10, 20))
print("Sum of 10, 20, 30 :", calculate_sum(10, 20, 30))
print("Sum of 1 to 5 :", calculate_sum(1, 2, 3, 4, 5))