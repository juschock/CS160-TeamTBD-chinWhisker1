#Begin Game - Welcome message - Version 2.0 from October 21st
print('**--** Welcome to the Tic-Tac-Toe challenge game! **--**')

# Import modules
import random 


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
    # store x entry into X list
    # store o entry in O list 
# 5. Check win
    # 5A. check rows
    # 5B. check columns
    # 5C. check diagnal
# 6. check tie
# 7. Flip tie

"""
Goals -  1. get the progrma to work before modifying the computer turn. Done 10/21/2019
         2. fix bugs
         3. implement AI to move strategiclly

!!! Current bugs !!!
                1. O winning is broken
                2. Tie deosn't seem to work
                3. AI is not currently operation, 
                4. Computer to replace 'O'
                5. line 114 could use some regex cleanup
"""
# --//-- Game code begins below --//-- #

##------- Global Variables -----##

# 1. set up game board
board = [ "-", "-", "-",
          "-", "-", "-",
          "-", "-", "-",]

# if the game is still going
game_still_going = True

# Who won? Or tie? 
winner = None

# whose turn is it?
current_player = "X"

## ------ End varablies declarations -------- ##

#-----*** Game Start ***------#
def play_game():
    display_board()
    print ('...which means I get to go first')

    # while game is active, loop over and over until game concludes
    while game_still_going:
        # Hanbdle a single turn of a player
        handle_turn(current_player)
        #Check if game has neded
        check_win()
        #flip to other player
        flip_player()
# The game has ended
    if winner == "X" or winner == "0":
        print(winner + " won!")
    elif winner == None:
        print("It's a Tie.")

# 2. display board
def display_board():
    print(' ')
    print(board[0] + " | " + board[1] + " | " + board[2], "   1, 2, 3")
    print(board[3] + " | " + board[4] + " | " + board[5], "   4, 5, 6")
    print(board[6] + " | " + board[7] + " | " + board[8], "   7, 8, 9")
    print('')

# 4. handle turn **Not used**
    # AI_turn()
    # human_turn()
    # print ('nice move, my turn...')
    # AI_turn()
    # human_turn()
    # print ('Sneaky Sneaky, my turn...')
    # AI_turn()
    # check_win()
    # display_board()

# Handle a single trun of a player
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    
    #while valid loop to require valid input is made
    valid= False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: #regex would be nicer
            position = input("Choose a position from 1-9: ")
        #provides the correct list index to corresponding input
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("you can't go there, try again")    
    board[position] = player #place the move on the board
    display_board() #call the board

# Handle a human turn
def human_turn(): #not used yet
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = "X"

def AI_turn(): #not used yet
    #check for near winning completions, if near choose
    position = random.randint(1,9)
    position = int(position) - 1
    board[position] = "O"
    

# 5. Check win
def check_win():
    # set up global variable for use
    global winner
    # 5A. check rows
    row_winner = check_rows()
    # 5B. check columns
    column_winner = check_columns()
    # 5C. check diagnal
    diag_winner = check_diag()
    #Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner == None

def check_rows():
    #setup global variable
    global game_still_going
    #check if rows are complete with winning combo
    row_1 = board[0]==board[1]==board[2] !="-"
    row_2 = board[3]==board[4]==board[5] !="-"
    row_3 = board[6]==board[7]==board[8] !="-"
    #if any row does have a match, flag for there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
     #setup global variable
    global game_still_going
    #check if rows are complete with winning combo
    column_1 = board[0]==board[3]==board[6] !="-"
    column_2 = board[1]==board[4]==board[7] !="-"
    column_3 = board[2]==board[5]==board[8] !="-"
    #if any row does have a match, flag for there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diag():
    #setup global variable
    global game_still_going
    #check if rows are complete with winning combo
    diag_1 = board[0]==board[4]==board[8] !="-"
    diag_2 = board[6]==board[4]==board[2] !="-"
    #if any row does have a match, flag for there is a win
    if diag_1 or diag_2:
        game_still_going = False
    # return the winner
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return

def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False

def flip_player():
    # global Variable Setting
    global current_player
    # if current player X, change to O
    if current_player == "X":
        current_player = "O"
        print("player O")
    # if current player O, chenge to X
    elif current_player =="O":
        current_player = "X"
        print("player X")
    return  

play_game()