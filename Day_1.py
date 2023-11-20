"""
Author: Stephanie Bernades
Date: Nov 2023
Description: This script calculates the fair amount each person should contribute to a bill, including a user-defined tip percentage.
Users are prompted to enter the total bill amount, choose a tip percentage (10%, 12%, or 15%), and specify the number of people splitting the bill.
The script then computes the tip, adds it to the total bill, divides the total by the number of people, and rounds the result to two decimal places.
The final output displays the equitable amount each person should pay.
"""

# Print a welcome message
print("Welcome to the tip calculator.")

# Get the total bill amount from the user
total_bill = float(input("What was the total bill? "))

# Get the tip percentage from the user
percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))

# Get the number of people splitting the bill
people = int(input("How many people split the bill? "))

# Calculate the tip amount
tip_amount = (total_bill * percentage) / 100

# Calculate the total bill with tip
total_with_tip = total_bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_with_tip / people

# Round the amount to two decimal places
amount_per_person_rounded = round(amount_per_person, 2)

# Display the amount each person should pay
print(f"Each person should pay: ${amount_per_person_rounded}")
