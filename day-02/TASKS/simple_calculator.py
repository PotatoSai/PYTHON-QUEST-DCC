# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.


print("SIMPLE CALCULATOR ALF")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
total = 0.0
operator = input("Enter the operator (+, -, x, /): ").lower()






# Write the code ↓ to perform the calculations based on the selected operation.


if operator == "+":
    total = first + second
elif operator == "-":
    total = first - second
elif operator == "x":
    total = first * second
elif operator == "/":
    total = first / second
else:
    print("\nInvalid operator.")





 
# Write the code ↓ to display the result.

print("\nThe result of %.1f %s %.1f is %.1f" % (first, operator, second, total))
# Select and employ a string concatenation method based on your personal preference and comfort level.







