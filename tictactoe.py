#tic tac toe game at the command line
#2021.10

#general program flow
#loop 9 times (until board full)
#print board
#take an input
#check valid input (if not valid, ask for a new input)
#update board with input
#check board status - win, tie
#toggle user
#repeat

from random import randrange
import numpy as np

def get_move():
    return (randrange(9)+1)

def print_board(board):
    """
    print board
    returns none
    args: board (np.array 2d)
    """

    for row in board:
        for col in row:
            print(col + ' ', end='')
        print('')

def toggle_player(player):
    """
    Toggle the player between "X" to "O"
    returns player ("X" or "O")
    args: toggled player ("X" or "O")
    """

    if player == 'X': return 'O'
    else: return 'X'

def update_board(position, board, player):
    """
    Update the board with the user input position if position not taken
    returns board, True=position taken or False=position not taken and board updated
    args: position (int 1-9, user input)
          board (np.array 2d)
          player ("X" or "O")
    """

    #make position 1-9 compatible with an 3x3 2d array indexed 0-8
    position = position - 1

    #logic to find row,col, uncomment 2 lines to print/test
    #print(position, 'int(/3) ', int(position/3))
    #print(position, '%3 ',position%3)

    #find position in array, obtain row/col index
    row = int(position/3)
    if position>2: col = position%3
    else: col = position

    #If position not taken, update board
    if board[row][col] == '-':
        board[row][col] = player
        return board, False

    #else position is taken, do not update board
    else:
        return board, True

def check_for_win(position, board, player):
    """
    check for wins on 3x3 board on rows,cols,diag,anti-diag
    args: position (int 1-9, user input)
          board (np.array 2d)
          player ("X" or "O")
    """

    #initialize win to False
    win = False

    #check win on rows
    for row in board:
        if np.all(row==player):
            win = True

    #check win on cols (index 0,1,2)
    for i in range(3):
        if(np.all(board[:,i]==player)):
            win = True

    #check win on diagonals
    if np.all(board.diagonal()==player):
        win = True

    #check win on anti-diagonals
    if np.all(np.fliplr(board).diagonal()==player):
        win = True

    return win


#main function to play tic tac toe
def main():

    print('Greetings: let\s play tic tac toe!')

    #intiialize board
    board = np.array([['-','-','-'],
            ['-','-','-'],
            ['-','-','-']])

    #initialize turn no to 0
    turn_no = 0

    #first player is always 'X'
    player = 'X'
    winner = None

    #play 9 turns or until q for quit is entered
    while turn_no < 9:

        #print board, ask for user input
        print_board(board)
        message = "Enter your move (1-9), q to quit: "
        if player == 'X':
            position = get_move()
        position = input(message)

        #quit game if q entered
        if position == 'q':
            print('quit')
            break


        try:
            #if user input integeter between 1 and 9 continue, else ask for a new input
            position = int(position)
            if position in [1,2,3,4,5,6,7,8,9]:

                #for valid input update board if position not taken
                board, position_taken = update_board(position, board, player)
                if position_taken:
                    print('Position taken, try again')

                else:
                    #check for a win and exit game if win
                    if check_for_win(position, board, player):
                        print_board(board)
                        print(player, ' won! Game Over')
                        winner = player
                        break
                    #if no win, toggle player and update turn no
                    turn_no+=1
                    player = toggle_player(player)

                    #if 9 turns and no winner, print board and declare a tie
                    if turn_no == 9:
                        print_board(board)
                        print('game complete, tie, no winner')
                        winner = 'tie'

            #if not an int between 1-9 then ask for a new input
            else:
                print('Invalid input, enter a number from 1 to 9 or q to quit')

        #exception for non-integer input or bug
        except:
            print('Exception! Invalid input. \nEnter a number from 1 to 9 or q to quit')

    return winner


if __name__ == "__main__":
    winner = main()
