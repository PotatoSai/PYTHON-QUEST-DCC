# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.

print("FACTORIAL CALCULATOR FOR ALF")


number = int(input("Enter a non-negative integer: "))
while number < 0:
    print("Please enter a non-negative integer.")
    number = int(input("Enter a non-negative integer: "))



# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.

total = 1

for i in range(1, number + 1):
    total *= i




# Write the code ↓ to display the factorial result.

print("The factorial of %d is: %d" % (number, total))
# Select and employ a string concatenation method based on your personal preference and comfort level.





