try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except ValueError:
    print("Invalid input!")

else:
    print("Input accepted successfully!")

finally:
    print("Program Finished.")