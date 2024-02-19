# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("VOWEL COUNT FOR ALF")

word = input("Enter the word to check: ")
wordLower = word.lower()







# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.


vowels = 'aeiou'
total = sum(wordLower.count(a) for a in vowels)





# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
        


print("The number of vowels in '%s' is: %d" % (word, total))




