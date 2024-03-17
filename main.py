import random

def print_board(board):
    print("------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def make_player_move(board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
        else:
            break

    board[row][col] = "X"

def make_computer_move(board):
    empty_cells = get_empty_cells(board)
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)

        # Player's turn
        make_player_move(board)

        if check_win(board):
            print_board(board)
            print("Player X wins!")
            break

        if len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

        # Computer's turn
        make_computer_move(board)

        if check_win(board):
            print_board(board)
            print("Computer O wins!")
            break

        if len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break
    print("Do you want to restart ? Yes or No")
    response = input()
    if response == "Yes":
        play_game()
    else:
        print("END GAME")

play_game()
