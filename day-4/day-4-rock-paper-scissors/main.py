rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

moves = [rock, paper, scissors]

# Player
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice > 2:
   print("You chose an invalid number, you lose")
   exit()

player_choice = moves[player_choice]
print(player_choice)

# Computer
cpu_choice = moves[random.randint(0,2)]
print(f"Computer chose:\n{cpu_choice}")

if player_choice == cpu_choice:
    print("Draw")
elif player_choice == rock and cpu_choice == paper:
    print("You lose")
elif player_choice == paper and cpu_choice == scissors:
    print("You lose")
elif player_choice == scissors and cpu_choice == rock:
    print("You Lose")
else:
    print("You win")
