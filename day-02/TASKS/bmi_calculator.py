# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.


print("BMI CALCULATOR ALF")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
status = ""







# Write the code ↓ to perform the calculations of user's BMI and categorize its status.

bmi = weight / (height * 2)

if bmi < 18.5:
    status = "UNDERWEIGHT"
elif bmi >= 18.5 or bmi <= 24.9:
    status = "NORMAL WEIGHT"
elif bmi >= 25 or bmi <= 29.9:
    status = "OVERWEIGHT"
else:
    status = "OBESITY"






# Write the code ↓ to display the user's BMI and its classification.

print("HEIGHT: %.2f - WEIGHT: %.2f" % (height, weight))
print("BMI: %.2f - NUTRITIONAL STATUS: %s" % (bmi, status))

# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.







