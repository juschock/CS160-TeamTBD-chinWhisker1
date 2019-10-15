print('Welcome to the Tic-Tac-Toe challenge game!')

# board = (0, 1, 2, 3, 4, 5,6 ,7 ,8, 9)
import random 
#Winning combinations(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 6), (3, 6, 9), (1, 5, 9), (7, 5, 3)


# Generates a random number between 
# a given positive range 
r1 = random.randint(0, 10)
opprand = input("Oppsing Human, please enter a number between 0-10: ")
crerand = input("Friendly Human, please enter a number between 0-10: ")
print("Random number between 0 and 10 is ", (r1))
if opprand == r1:
    print (opprand + "is correct and you get first move")
    print ("So sorry, I get to go first")
    # go to first move
else:
    print (crerand + " is close enough for the home team") 


# ------working up to here---------

    # set up game board
board = []
for x in range(0,5):
    board.append(["0"] * 5)
def print_board(board):
    for row in board:
        print "".join(row)
print_board(board)
    #Computer goes first
