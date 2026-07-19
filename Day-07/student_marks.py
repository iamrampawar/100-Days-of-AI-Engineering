marks = [85,72,90,66,78]

print("Student marks")
print(marks)

print("\n marks of each student:")
for mark in marks:
    print(mark)

total = 0

for mark in marks:
    total = total + mark

print("\n Total marks :",total)


average = total/len(marks)
print("\n Average marks :", average)



highest = max(marks)
lowest = min(marks)

print("\nhighest marks :",highest)
print("lowest marks :",lowest)