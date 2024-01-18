"""
Author: Stephanie Bernades
Date: January 17, 2024
Description: This program generates a random password when given how many letters, symbols and numbers.
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#get length of all lists
len_letters = len(letters)-1
len_symbols = len(symbols)-1
len_numbers = len(numbers)-1


result1 = []

#Gets the letters
for x in range(0, nr_letters):
    number = random.randint(0, len_letters)
    letter = letters[number]
    result1.append(letter)

#Symbols
for x in range(0, nr_symbols):
    number = random.randint(0, len_symbols)
    symbol = symbols[number]
    result1.append(symbol)

#numbers
for x in range(0, nr_numbers):
    number = random.randint(0, len_numbers)
    num = numbers[number]
    result1.append(num)

#Shuffles the elements in the list
random.shuffle(result1)
word = ""
#Goes through each element and pushes each into a string
for x in result1:
    word += str(x)

print(word)