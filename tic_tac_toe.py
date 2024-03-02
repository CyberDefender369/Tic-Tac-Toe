#list of 9 empty spaces for board position
board = [" " for i in range(9)]

#making shape of board
def board_shape():
    row1 = f"	|{board[0]}|{board[1]}|{board[2]}|"
    row2 = f"	|{board[3]}|{board[4]}|{board[5]}|"
    row3 = f"	|{board[6]}|{board[7]}|{board[8]}|"
    
    print(row1)
    print(row2)
    print(row3)
    print()

#setting up the player's icon
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
        
    print(f"Player {number}, you're up!")

    choice = int(input("Choose your position (1-9): ").strip())
    
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is not available!")
  
#checking win conditions
def victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

#checking draw condtion
def draw():
    if " " not in board:
        return True
    else:
        return False
    
#updating player's postions on the board
while True:
    board_shape()
    player_move("X")
    board_shape()
    if victory("X"):
        print("Player 1 wins! They never stood a chance!")
        break
    elif draw():
        print("Unfortunately, it is a draw!")
        break
    player_move("O")
    if victory("O"):
        board_shape()
        print("Player 2 wins! They never stood a chance!")
        break
    elif draw():
        print("Unfortunately, it is a draw!")
        break