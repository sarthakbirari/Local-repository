def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],

        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],

        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],

        
    ]
    return [player, player, player] in win_states
def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"player {current_player}'s turn")

        try:
            row = int(input("enter row (0-2): "))
            col = int(input("enter column (0-2): "))
        except ValueError:
            print("Invalid input! Use numbers 0-2.")
            continue
        if row not in range(3) or col not in range (3):
            print("out of bounds! try again.")
            continue 
        if board[row][col] != " ":
            print("cell already taken! try again.")
            continue 
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("its a draw!")
            break 

        current_player = "O" if current_player =="x" else "X"


tic_tac_toe()       
        