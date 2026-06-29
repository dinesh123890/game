# Version 3.0
>>>>>>> confict-test2
# ================================
# TIC TAC TOE — Python Beginner Game
# Tic Tac Toe Game - Version 1.0 - Made by Dinesh
# Tic Tac Toe Game - Version 1.0 - Made by Dinesh
# ================================

# The board — a list of 9 boxes
# Index:  0 | 1 | 2
#         3 | 4 | 5
#         6 | 7 | 8
board = [" "] * 9   # Creates a list with 9 empty spaces


def print_board():
    """Print the board in a readable grid format"""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    """Check if the given player (X or O) has won"""

    # All possible winning combinations (rows, columns, diagonals)
    wins = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # middle column
        [2, 5, 8],  # right column
        [0, 4, 8],  # diagonal top-left to bottom-right
        [2, 4, 6],  # diagonal top-right to bottom-left
    ]

    # Check if player occupies all 3 spots in any winning combo
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True  # This player won!

    return False  # No win yet


def check_draw():
    """Check if the board is full with no winner — a draw"""
    return " " not in board  # If no empty space left, it's a draw


def play_game():
    """Main game loop"""
    print("=== TIC TAC TOE ===")
    print("Positions: 1-9 (top-left to bottom-right)")
    print("Example: type 5 to place in the center")

    current_player = "X"  # X always goes first

    while True:
        print_board()
        print(f"Player {current_player}'s turn")

        # Get input from the player
        try:
            move = int(input("Enter position (1-9): ")) - 1  # -1 because list starts at 0
        except ValueError:
            print("Please enter a number between 1 and 9")
            continue

        # Check if position is valid
        if move < 0 or move > 8:
            print("Invalid! Choose between 1 and 9")
            continue

        # Check if position is already taken
        if board[move] != " ":
            print("That spot is taken! Choose another.")
            continue

        # Place the player's mark on the board
        board[move] = current_player

        # Check if this move won the game
        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} WINS!")
            break

        # Check if it's a draw
        if check_draw():
            print_board()
            print("It's a DRAW! Well played both!")
            break

        # Switch to the other player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # Ask to play again
    again = input("\nPlay again? (yes/no): ").lower()
    if again == "yes":
        board[:] = [" "] * 9   # Reset the board
        play_game()             # Start a new game
    else:
        print("Thanks for playing!")


# Start the game
play_game()