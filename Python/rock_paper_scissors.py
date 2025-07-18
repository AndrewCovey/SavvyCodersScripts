# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:

import random

options = ['rock', 'paper', 'scissors']

player1 = random.choice(options)
player2 = random.choice(options)

def state_choice(player, choice):
    print(player + "has selected: " + str(choice))
    return

def state_winner(player1, player2):
    if player1 == player2:
        print(f"Both chose {player1}. It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        print(f"Player 1 chose {player1}, Player 2 chose {player2}. Player 1 wins!")
    else:
        print(f"Player 1 chose {player1}, Player 2 chose {player2}. Player 2 wins!")
    return

state_choice("Player 1 ", player1)
state_choice("Player 2 ", player2)
state_winner(player1, player2)