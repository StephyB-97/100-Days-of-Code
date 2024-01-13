import random

#get user input
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))


#ascii options
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

#generate computer input
computer = random.randint(0,2)

print(options[player])
print("Computer chose")
print(options[computer])

#tie between player and computer
if player == computer:
    print("Its a tie!")
#All the winning options for the user
elif (player == 0 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 0):
    print("You win!")
else:
    print("Computer wins!")