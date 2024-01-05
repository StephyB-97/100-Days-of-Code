# Love Calculator Program
# Author: Stephanie Bernades
# Date: 2024-01-04
# Description: This program calculates a love score based on the names entered.
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?


# Base words
true = "true"
love = "love"

#word count
count1 = 0   # word count for name 1 and "true"
count2 = 0   # word count for name 2 and "true"
count3 = 0   # word count for name 2 and "love"
count4 = 0   # word count for name 2 and "love"

# count the letters in name1 that appear in "true"
for letter in name1.lower():
  if letter in true:
    count1 +=1

# count the letters in name2 that appear in "true"
for letter in name2.lower():
  if letter in true:
    count2 +=1

# count the letters in name1 that appear in "love"
for letter in name1.lower():
  if letter in love:
    count3 += 1

# count the letters in name1 that appear in "love"
for letter in name2.lower():
  if letter in love:
    count4 +=1


# Addition of the count for the two names in the words "true" and "love" concatanated to make a two digit number
two_digit = int(str(count1 + count2) + str(count3 + count4))

# Option if calculation is less than 10 and greater than 90
if two_digit > 10 or two_digit < 90:
  print(f"Your score is {two_digit}, you go together like coke and mentos.")

# Option if calculation is between 40 and 50
elif two_digit >= 40 and two_digit <= 50:
  print(f"Your score is {two_digit}, you are alright together.")

# Option if the calculation is none of the two mentioned previously
else:
  print(f"Your score is {two_digit}")
