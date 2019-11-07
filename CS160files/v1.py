#Begin Game - Welcome message - Version 1.1 from October 15th
print('Welcome to the Tic-Tac-Toe challenge game!')

# board = (0, 1, 2, 3, 4, 5, 6 ,7 ,8, 9)
import random 
#Winning combinations

# Generates a random number between 
# a given positive range 
r1 = random.randint(0, 10)
opprand = input("Opposing Human, please enter a number between 0-10: ")
crerand = input("Friendly Human, please enter a number between 0-10: ")
print("Random number between 0 and 10 is ", (r1))
if opprand == r1:
    print (opprand + "is correct and you get first move")
    print ("So sorry, I get to go first")
    # go to first move
else:
    print (crerand + " is close enough for the home team") 

#--# Program Outline #--#
# 1. Create Board
# 2. Display Board
# 3. Play game
# 4. Handle input/turn
# 5. Check win
    # 5A. check rows
    # 5B. check columns
    # 5C. check diagnal
# 6. check tie
# 7. Flip tie


# ------working up to here---------#
# print ('...which means I get to go first')

# 1. set up game board
board = [ "-", "-", "-",
          "-", "-", "-",
          "-", "-", "-",]
# 2. display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()
    print ('...which means I get to go first')
# 4. handle turn
    AI_turn()
    human_turn()
    print ('nice move, my turn...')
    AI_turn()
    human_turn()
    print ('Senaky Sneaky, my turn...')
    AI_turn()
# 5. Check win


def human_turn():
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = "X"

    display_board()

def AI_turn():
    #check for near winning completions, if near choose
    position = random.randint(1,9)
    position = int(position) - 1
    board[position] = "O"

    display_board()

def check_win():
    winCombo=[(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 6), (3, 6, 9), (1, 5, 9), (7, 5, 3)]
    if board[0] == winCombo[0:9]:
        print ("Congrats!")
    else:
        print('keep going')
play_game()





