from IPython.display import clear_output

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    


    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    choice = ''
    
    while not (choice == 'X' or choice == 'O'):
        choice = input('Player 1: Do you want to be X or O? ').upper()

    if choice == 'X':
        print("Great! You are Player 'X'!")
        return ('X', 'O')
    else:
        print("Great! You are Player 'O'!")
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the top
    (board[7] == mark and board[4] == mark and board[1] == mark) or # up the up the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # up the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # up the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # upward diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # upward diagonal

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    while board[position] == ' ':
        return 'Open space'

def full_board_check(board):
    for every_position in range(1,10):
        if space_check(board, every_position):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        if not position:
            print("Please type a number from 1 to 9, you dipshit.")
        else:
            pass
        
    return position

def replay():
    return input("Please type the key 'Y' to continue, or 'N' to quit.").lower().startswith('y')

from time import sleep
print('Welcome to Tic Tac Toe!')

while True:
    gameboard = [' '] * 10
    import time
   
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    player1, player2 = player_input() 
    whos_first = choose_first()
    print(f"{whos_first}" + " starts!")
    time_suspension = time.sleep(2) #This works like a charm!


    while game_on:

        if whos_first == 'Player 1':

            display_board(gameboard)
            position = player_choice(gameboard)
            place_marker(gameboard, player1, position)

            if win_check(gameboard, player1):
                display_board(gameboard)
                print('Player 1 won!')
                game_on = False

            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print("It's a draw!")
                    break
                else:
                    whos_first = 'Player 2'
        else:
            display_board(gameboard)
            position = player_choice(gameboard)
            place_marker(gameboard, player2, position)

            if win_check(gameboard, player2):
                display_board(gameboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print("It's a draw!")
                    break
            
                else:
                    whos_first = 'Player 1'

    
    if not replay():
        break
