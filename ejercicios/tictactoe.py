def display_board(board):
    print("  |  |")
    for i in range(3):
        print(f"{board[3*i]} | {board[3*i+1]} | {board[3*i+2]}")
        print("  |  |")


def player_move(board, player):
    while True:
        move = int(input(f"player {player}, ingresa tu mov(1-9)"))-1
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = player 
            return 
        print("esto esta mal")


def check_win(board, player):
    win_condition = ((0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6))
    
    for condition in win_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tableroLleno(board):
    for cell in board:
        if cell == " ":
            return False
    return True

board = [" "] * 9
player  = "X"

while True:
    display_board(board)
    player_move(board, player)
    if check_win(board, player):
        print(f"player {player} has won")
        break
    elif tableroLleno(board):
        display_board(board)
        print(f"draw")
        break
    player = "O" if player == "X" else "X"