import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.

print("HYPOTENUSE CALCULATOR FOR ALF")

sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))
total = 0.0




# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.




total = math.sqrt(math.pow(sideA, 2) + math.pow(sideB, 2))




# Write the code ↓ to display the calculated hypotenuse.

print("The hypothenuse of the right-angled triangle is: %.2f" % total)
# Select and employ a string concatenation method based on your personal preference and comfort level.






