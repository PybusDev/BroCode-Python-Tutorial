# BMI = Body Mass Index (Measure of Height and Weight to estimate body fat %)
#       General estimate that doesn't account muscle vs fat
#       Children have a different BMI chart
#       BMI = weight(lbs/kg) / height(in/m)^2


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / height ** 2

print(f"Your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")