#Import the necessary libraries
from time import time
from queue import Queue
#Import the necessary libraries
import numpy as np
from math import inf as infinity
#Set the Empty Board
game_state = [[' ',' ',' '],
 [' ',' ',' '],
 [' ',' ',' ']]
#Create the Two Players as 'X'/'O'
players = ['X','O']
#Method for checking the correct move on Tic-Tac-Toe
def play_move(state, player, block_num):
 if state[int((block_num-1)/3)][(block_num-1)%3] == ' ':
 #TODO: Assign the player move on the current position of Tic-Tac-Toe if condition is True
 state[int((block_num-1)/3)][(block_num-1)%3] = player
 else:
 block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
 play_move(state, player, block_num)
 #TODO: Recursively call the play_move
#Method to copy the current game state to new_state of Tic-Tac-Toe
def copy_game_state(state):
 new_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
 for i in range(3):
 for j in range(3):
 #TODO: Copy the Tic-Tac-Toe state to new_state
 new_state[i][j] = state[i][j]
 #TODO: Return the new_state
 return new_state
#Method to check the current state of the Tic-Tac-Toe
def check_current_state(game_state):
 #TODO: Set the draw_flag to 0
 draw_flag = 0
 for i in range(3):
 for j in range(3):
 if game_state[i][j] == ' ':
 draw_flag = 1

 if draw_flag == 0:
 return None, "Draw"

 # Check horizontals in first row
 if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and
game_state[0][0] != ' '):
 return game_state[0][0], "Done"
 #TODO: Check horizontals in second row
 if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and
game_state[1][0] != ' '):
 return game_state[1][0], "Done"
 #TODO: Check horizontals in third row
 if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and
game_state[2][0] != ' '):
 return game_state[2][0], "Done"

 # Check verticals in first column
 if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and
game_state[0][0] != ' '):
 return game_state[0][0], "Done"
 # Check verticals in second column
 if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and
game_state[0][1] != ' '):
 return game_state[0][1], "Done"
 # Check verticals in third column
 if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and
game_state[0][2] != ' '):
 return game_state[0][2], "Done"

 # Check left diagonal
 if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and
game_state[0][0] != ' '):
 return game_state[1][1], "Done"
 # Check right diagonal
 if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and
game_state[2][0] != ' '):
 return game_state[1][1], "Done"

 return None, "Not Done"
#Method to print the Tic-Tac-Toe Board
def print_board(game_state):
 print('----------------')
 print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + '
|')
 print('----------------')
 print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + '
|')
 print('----------------')
 print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + '
|')
 print('----------------')
#Method for implement the Minimax Algorithm
def getBestMove(state, player):
 #TODO: call the check_current_state method using state parameter
 winner_loser , done = check_current_state(state)
 #TODO:Check condition for winner, if winner_loser is 'O' then Computer won
 #else if winner_loser is 'X' then You won else game is draw
 if done == "Done" and winner_loser == 'O': # If AI won
 return (1,0)
 elif done == "Done" and winner_loser == 'X': # If Human won
 return (-1,0)
 elif done == "Draw": # Draw condition
 return (0,0)

 #TODO: set moves to empty list
 moves = []
 #TODO: set empty_cells to empty list
 empty_cells = []

 #Append the block_num to the empty_cells list
 for i in range(3):
 for j in range(3):
 if state[i][j] == ' ':
 empty_cells.append(i*3 + (j+1))

 #TODO:Iterate over all the empty_cells
 for empty_cell in empty_cells:
 #TODO: create the empty dictionary
 move = {}

 #TODO: Assign the empty_cell to move['index']
 move['index'] = empty_cell

 #Call the copy_game_state method
 new_state = copy_game_state(state)

 #TODO: Call the play_move method with new_state,player,empty_cell
 play_move(new_state, player, empty_cell)

 #if player is computer
 if player == 'O':
 #TODO: Call getBestMove method with new_state and human player ('X') to make more
depth tree for human
 result,_ = getBestMove(new_state, 'X')
 move['score'] = result
 else:
 #TODO: Call getBestMove method with new_state and computer player('O') to make
more depth tree for computer
 result,_ = getBestMove(new_state, 'O')
 move['score'] = result

 moves.append(move)
 # Find best move
 best_move = None
 #Check if player is computer('O')
 if player == "O":
 #TODO: Set best as -infinity for computer
 best = -infinity
 for move in moves:
 #TODO: Check if move['score'] is greater than best
 if move['score'] > best:
 best = move['score']
 best_move = move['index']

 else:
 #TODO: Set best as infinity for human
 best = infinity
 for move in moves:
 #TODO: Check if move['score'] is less than best
 if move['score'] < best:
 best = move['score']
 best_move = move['index']
 return (best, best_move)
# Now PLaying the Tic-Tac-Toe Game
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':
 #Set the empty board for Tic-Tac-Toe
 game_state = [[' ',' ',' '],
 [' ',' ',' '],
 [' ',' ',' ']]
 #Set current_state as "Not Done"
 current_state = "Not Done"
 print("\nNew Game!")


 #print the game_state
 print_board(game_state)

 #Select the player_choice to start the game
 player_choice = input("Choose which player goes first - X (You) or O(Computer): ")

 #Set winner as None
 winner = None

 #if player_choice is ('X' or 'x') for humans else for computer
 if player_choice == 'X' or player_choice == 'x':
 #TODO: Set current_player_idx is 0
 current_player_idx = 0
 else:
 #TODO: Set current_player_idx is 1
 current_player_idx = 1

 while current_state == "Not Done":
 #For Human Turn
 if current_player_idx == 0:
 block_choice = int(input("Your turn please! Choose where to place (1 to 9): "))
 #TODO: Call the play_move with parameters as game_state
,players[current_player_idx], block_choice
 play_move(game_state ,players[current_player_idx], block_choice)
 else: # Computer turn
 _,block_choice = getBestMove(game_state, players[current_player_idx])
 #TODO: Call the play_move with parameters as game_state
,players[current_player_idx], block_choice
 play_move(game_state ,players[current_player_idx], block_choice)
 print("AI plays move: " + str(block_choice))
 print_board(game_state)
 #TODO: Call the check_current_state function for game_state
 winner, current_state = check_current_state(game_state)
 if winner is not None:
 print(str(winner) + " won!")
 else:
 current_player_idx = (current_player_idx + 1)%2

 if current_state == "Draw":
 print("Draw!")

 play_again = input('Wanna try again?(Y/N) : ')
 if play_again == 'N':
 print('Thank you for playing Tic-Tac-Toe Game!!!!!!!')
