import numpy as np

marks = np.array([85, 90, 88, 76, 95, 81])

print("Original Array:")
print(marks)

print("\nReshape (2 x 3):")
print(marks.reshape(2,3))

print("\nReshape (3 x 2):")
print(marks.reshape(3,2))

print("\nAuto Reshape:")
print(marks.reshape(2,-1))