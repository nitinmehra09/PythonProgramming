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
    else:
        if(player1_choice == 1 and player2_choice == -1):
            return "You wins!"
        elif(player1_choice == 1 and player2_choice == 0):
            return "Computor wins!"
        elif(player1_choice == 0 and player2_choice == -1):
            return "Computor wins!" 
        elif(player1_choice == 0 and player2_choice == 1):
            return "You wins!" 
        elif(player1_choice == 1 and player2_choice == -1):
            return "You wins!" 
        elif(player1_choice == 1 and player2_choice == 0):
            return "Computor wins!" 

print('''
   1. Snake (1)
   2. Water (-1)
   3. Gun (0)
''')

player1_choice = int(input("Player 1, choose your weapon: "))

player2_choice = random.choice([1,0,-1])

print(play_game(player1_choice, player2_choice))
