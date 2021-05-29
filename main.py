import random

rock = '''
_______
---' ____)
(_____)
(_____)
(____)
---.__(___)
'''
paper = '''
_______
---' ____)____
______)
_______)
_______)
---.__________)
'''
scissors = '''
_______
---' ____)____
______)
__________)
(____)
---.__(___)
'''
game_images = [rock, paper, scissors]
game_name = {0: 'rock', 1: 'paper', 2: 'scissors'}
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("Invalid number, Please try again!")
else:
    print(f'You chose: {game_name[user_choice]}')
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f'Computer chose: {game_name[computer_choice]}')
    print(game_images[user_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == computer_choice:
        print("You draw, Try again")
    else:
        print("You loose")
