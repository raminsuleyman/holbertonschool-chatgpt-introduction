#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("--+---+--")

def check_winner(board):
    # Rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # X or O

    # Columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def get_input(player):
    while True:
        try:
            row = int(input(f"Enter row (0,1,2) for player {player}: "))
            col = int(input(f"Enter column (0,1,2) for player {player}: "))
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Coordinates must be 0, 1, or 2.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    winner = None

    while moves < 9 and winner is None:
        print_board(board)
        row, col = get_input(player)

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
            winner = check_winner(board)
            if winner:
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
