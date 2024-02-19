# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.



print("PALINDROME CHECKER FOR ALF")

word = input("Enter the word to check: ")
wordLower = word.lower()



# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.

reverseWord = ""



for char in wordLower:
    reverseWord = char + reverseWord




# Write the code ↓ to display whether the entered word is a palindrome or not.
# Select and employ a string concatenation method based on your personal preference and comfort level.





if wordLower == reverseWord:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


