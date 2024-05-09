import random

"""
    Print the current state of the Tic Tac Toe board.

    Parameters:
    board (list of lists): The 3x3 Tic Tac Toe board.
    """


def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")


"""
    Check if a player has won the game.

    Parameters:
    board (list of lists): The 3x3 Tic Tac Toe board.
    player (str): The player's marker ('X' or 'O').

    Returns:
    bool: True if the player has won, False otherwise.
    """


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


"""
    Check if the Tic Tac Toe board is full.

    Parameters:
    board (list of lists): The 3x3 Tic Tac Toe board.

    Returns:
    bool: True if the board is full, False otherwise.
    """


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


"""
    Get the player's move.

    Parameters:
    board (list of lists): The 3x3 Tic Tac Toe board.

    Returns:
    tuple: The row and column of the player's move.
    """


def player_move(board):
    row = int(input("Enter row number (1-3): ")) - 1
    col = int(input("Enter column number (1-3): ")) - 1
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        return row, col
    else:
        print("Invalid move. Please try again.")


"""
    Get the computer's move.

    Parameters:
    board (list of lists): The 3x3 Tic Tac Toe board.

    Returns:
    tuple: The row and column of the computer's move.
    """


def computer_move(board):
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(available_moves)


def play_game():
    board = [[" "] * 3 for i in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's turn
        row, col = player_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        print("Computer's turn:")
        row, col = computer_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("You Lose!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break


play_game()
