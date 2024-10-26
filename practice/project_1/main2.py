'''
Snake = 1
Water = -1
Gun = 0
Snake vs. Water: If a player chooses Snake and their opponent chooses Water, Snake wins because Snake drinks the Water.
Water vs. Gun: If a player chooses Water and their opponent chooses Gun, Water wins because the Gun will drown in Water.
Gun vs. Snake: If a player chooses Gun and their opponent chooses Snake, Gun wins because Gun shoots Snake.
'''
import random

def play_game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 1 and player2_choice == -1) or (player1_choice == 0 and player2_choice == 1) or (player1_choice == -1 and player2_choice == 0):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

print('''
   1. Snake (1)
   2. Water (-1)
   3. Gun (0)
''')

try:
    player1_choice = int(input("Player 1, choose your weapon (1, -1, 0): "))
    if player1_choice not in [1, -1, 0]:
        raise ValueError("Invalid choice. Please choose 1, -1, or 0.")
except ValueError as e:
    print(e)
    exit()

player2_choice = random.choice([1, -1, 0])

print(f"Player 2 chose: {player2_choice}")
print(play_game(player1_choice, player2_choice))