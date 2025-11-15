# A simple command-line Tic-Tac-Toe game in Python

def print_board(board):
    """
    This function prints out the Tic-Tac-Toe board.
    The board is represented as a list of 9 strings.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """
    This function checks if the given player ('X' or 'O') has won.
    It checks all 8 possible winning combinations.
    """
    # Check rows
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player):
        return True
    # Check columns
    elif (board[0] == player and board[3] == player and board[6] == player) or \
         (board[1] == player and board[4] == player and board[7] == player) or \
         (board[2] == player and board[5] == player and board[8] == player):
        return True
    # Check diagonals
    elif (board[0] == player and board[4] == player and board[8] == player) or \
         (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def check_draw(board):
    """
    This function checks if the game is a draw (i.e., the board is full).
    If it finds any spot that is still a number, the game is not a draw.
    """
    for spot in board:
        if spot.isdigit(): # Checks if the spot is still a number (e.g., "1", "2", ...)
            return False
    return True # If no spots are numbers, the board is full

def main_game():
    """
    This is the main function that runs the game loop.
    """
    
    # Initialize the board with numbers 1-9
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"
    game_is_running = True

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while game_is_running:
        
        # --- Get Player Input ---
        move = input(f"Player '{current_player}', enter your move (1-9): ")

        # --- Validate Input ---
        if not move.isdigit():
            print("That's not a valid number. Please try again.")
            continue # Skip the rest of the loop and ask again
        
        move_index = int(move) - 1 # Convert "1" to index 0, "9" to index 8, etc.

        if move_index < 0 or move_index > 8:
            print("That number is out of bounds. Please choose 1-9.")
            continue
        
        if board[move_index] in ["X", "O"]:
            print("That spot is already taken! Try again.")
            continue
        
        # --- Update Board ---
        board[move_index] = current_player
        print_board(board)

        # --- Check for Winner ---
        if check_win(board, current_player):
            print(f"Congratulations! Player '{current_player}' wins!")
            game_is_running = False
        
        # --- Check for Draw ---
        elif check_draw(board):
            print("It's a draw! Good game.")
            game_is_running = False
        
        # --- Switch Player ---
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

# This line tells Python to run the main_game() function
# when you execute the script directly.
if __name__ == "__main__":
    main_game()
