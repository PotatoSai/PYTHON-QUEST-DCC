# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.

print("PERFECT NUMBER DETEMINATOR FOR ALF")

number = int(input("Enter a non-negative integer: "))

while number < 0:
    print("Please enter a non-negative integer.")
    number = int(input("Enter a non-negative integer: "))









# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i





# Write the code ↓ to display the Perfect Number check result.

if number == total:
    print("%d is a Perfect Number" % number)
else:
    print("%d is not a Perfect Number" % number)

# NOTE : You can use if-else statement or ternary operator to display the result.






