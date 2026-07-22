# Day 10 - Random Module

import random

print("Random Number (1 to 10):", random.randint(1, 10))

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Random Fruit:", random.choice(fruits))

numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)

print("Shuffled List:", numbers)