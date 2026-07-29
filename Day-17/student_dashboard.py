import numpy as np

# Rows = Students
# Columns = Math, Science, English

marks = np.array([
    [85, 90, 88],
    [76, 95, 81],
    [92, 89, 94]
])

print("=" * 40)
print("      STUDENT DASHBOARD")
print("=" * 40)

print("\nStudent Marks:")
print(marks)

print("\nShape:", marks.shape)
print("Dimensions:", marks.ndim)
print("Total Elements:", marks.size)

print("\nAverage Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("\nTranspose:")
print(marks.T)

print("=" * 40)
print("Dashboard Generated Successfully!")
print("=" * 40)