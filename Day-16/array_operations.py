import numpy as np

marks = np.array([85, 90, 76, 95, 88])

print("Original Array:")
print(marks)

print("\nAdd 5 Marks:")
print(marks + 5)

print("\nSubtract 5:")
print(marks - 5)

print("\nDouble Marks:")
print(marks * 2)

print("\nHalf Marks:")
print(marks / 2)

print("\nAverage Marks:")
print(np.mean(marks))

print("\nHighest Marks:")
print(np.max(marks))

print("\nLowest Marks:")
print(np.min(marks))

print("\nTotal Marks:")
print(np.sum(marks))