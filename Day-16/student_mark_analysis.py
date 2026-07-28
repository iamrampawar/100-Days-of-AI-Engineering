import numpy as np

# Student Marks
marks = np.array([85, 90, 76, 95, 88])

print("=" * 40)
print("      STUDENT MARKS ANALYSIS")
print("=" * 40)

print(f"Marks               : {marks}")
print(f"Number of Students  : {len(marks)}")
print(f"Total Marks         : {np.sum(marks)}")
print(f"Average Marks       : {np.mean(marks):.2f}")
print(f"Highest Marks       : {np.max(marks)}")
print(f"Lowest Marks        : {np.min(marks)}")

print("\nStudents scoring above 90:")
print(marks[marks > 90])

print("\nStudents scoring below 80:")
print(marks[marks < 80])

print("\nStudents scoring 80 or above:")
print(marks[marks >= 80])

print("=" * 40)
print("Analysis Completed Successfully!")
print("=" * 40)