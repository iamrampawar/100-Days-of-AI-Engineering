def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Ennter your weight(kg) :"))
height = float(input("Enter your heitht(meters) :"))

bmi = calculate_bmi(weight,height)
 
print(f"\n Your BMI is: {bmi:.2f}")

if bmi<18.5:
    print("Category : Underweight")
elif bmi<25:
    print("Category: Normal weight")

elif bmi<30:
    print("Category : Overweight")
else:
    print("catagory : obese")
