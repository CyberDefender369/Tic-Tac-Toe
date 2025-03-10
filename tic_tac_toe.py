# This script implements a simple Tic Tac Toe game for two players.

import random

def board_shape(board):
    '''Prints out the current state of the board.'''
    
    row1 = f'|{board[0]}|{board[1]}|{board[2]}|'
    row2 = '-------'
    row3 = f'|{board[3]}|{board[4]}|{board[5]}|'
    row4 = '-------'     
    row5 = f'|{board[6]}|{board[7]}|{board[8]}|'
    
    print()
    print(row1)
    print(row2)
    print(row3) 
    print(row4)
    print(row5)
    print()

def assign_symbols():
    '''Assigns a symbol (X or O) to each player and validates user input.'''
    
    while True:
        symbol = input('\nChoose your symbol (X or O): ').lower()
        if symbol not in ['x', 'o']:
            print('\nInvalid input. Please enter X or O.')
        elif symbol == 'x':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_symbol(board, symbol, position):
    '''Places the player's symbol at the specified position on the board.'''
    
    board[position] = symbol
    
def check_win_conditions(board, symbol):
    '''Checks if the given symbol has met any of the winning conditions.'''

    return ((board[0] == symbol and board[1] == symbol and board[2] == symbol) or # top row
            (board[3] == symbol and board[4] == symbol and board[5] == symbol) or # middle row
            (board[6] == symbol and board[7] == symbol and board[8] == symbol) or # bottom row
            (board[0] == symbol and board[4] == symbol and board[8] == symbol) or # diagonal left to right
            (board[2] == symbol and board[4] == symbol and board[6] == symbol) or # diagonal right to left
            (board[0] == symbol and board[3] == symbol and board[6] == symbol) or # left column
            (board[1] == symbol and board[4] == symbol and board[7] == symbol) or # middle column
            (board[2] == symbol and board[5] == symbol and board[8] == symbol)) # right column

def check_draw_condition(board):
    '''Checks if the board is full, indicating a tie.'''
    
    if ' ' in board:
        return False
    else:
        return True
    
def determine_first_player():
    '''Randomly selects which player goes first.'''
    
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def is_space_available(board, position):
    '''Checks if the specified position on the board is available.'''

    return board[position] == ' '
        
def get_player_choice(board):
    '''Prompts the player to choose a position on the board and validates the input.'''
    
    while True:
        try:
            position = int(input('\nChoose your position (1-9): '))
            if position not in range(1, 10):
                print('\nInvalid input. Please enter a number between 1 and 9.')
            elif is_space_available(board, position - 1 ) == False:
                print('\nPosition already taken. Please try again.')
            else:
                return position - 1
        except ValueError:
            print('\nInvalid input. Please enter a number between 1 and 9.')

def ask_replay():
    '''Asks the players if they want to play another game.'''

    while True:
        choice = input('\nPlay again? Enter y/n: ').lower()
        if choice not in ['y', 'n']:
            print('\nInvalid input. Please enter y or n.')
        else:
            return choice == 'y'

def handle_turn(board, player, symbol):
    '''Handles a single turn for a player.'''

    board_shape(board)
    print(f'{player}, it is your turn.')
    position = get_player_choice(board)
    place_symbol(board, symbol, position)
    
    if check_win_conditions(board, symbol):
        board_shape(board)
        print(f'{player} won.')
        return True
    elif check_draw_condition(board):
        board_shape(board)
        print("\nIt's a tie!")
        return True
    else:
        return False

# Main game logic
while True:
    print('\nWelcome to Tic Tac Toe!')
    print('-----------------------')
    
    # Initialize the game board
    board = [' '] * 9
    
    # Assign symbols to players
    player1, player2 = assign_symbols()
    
    # Determine who goes first
    turn = determine_first_player()
    print(f'\nPlayer 1, you are {player1}. Player 2, you are {player2}.')
    print(f'\n{turn} goes first.')
    
    # Game loop
    game_over = False
    while not game_over:    
        if turn == 'Player 1':
            game_over = handle_turn(board, 'Player 1', player1)
            turn = 'Player 2'
        else:
            game_over = handle_turn(board, 'Player 2', player2)
            turn = 'Player 1'
        
    # Ask if players want to play again
    if ask_replay() == False:
        print('\nThanks for playing!')
        break