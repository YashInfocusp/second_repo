# Tic Tac Toe Game Logic

def initialize_board():
    """Initializes an empty 3x3 Tic Tac Toe board."""
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    """Prints the Tic Tac Toe board to the console."""
    for row in board:
        print("|".join(row))
        print("-----")

if __name__ == '__main__':
    # Example usage:
    board = initialize_board()
    display_board(board)
    # Example usage (to be replaced by the main game loop):
    # board = initialize_board()
    # display_board(board)
    # board[0][0] = "X"
    # board[1][1] = "O"
    # display_board(board)
    main_game_loop() # Add this call

def main_game_loop():
    while True:
        board = initialize_board()
        current_player = "X"
        game_over = False

        while not game_over:
            display_board(board)
            print(f"Player {current_player}'s turn")

            while True:
                try:
                    row = int(input("Enter row (1-3): ")) - 1
                    col = int(input("Enter column (1-3): ")) - 1

                    if not (0 <= row < 3 and 0 <= col < 3):
                        print("Invalid input. Row and column must be between 1 and 3.")
                        continue

                    if not is_valid_move(board, row, col):
                        print("Invalid move. The cell is already taken or out of bounds.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers for row and column.")

            make_move(board, row, col, current_player)

            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_board_full(board):
                display_board(board)
                print("It's a draw!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == '__main__':
    main_game_loop()

def is_valid_move(board, row, col):
    """Checks if the cell (row, col) is a valid move."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def make_move(board, row, col, player):
    """Places the player's mark on the board at (row, col)."""
    board[row][col] = player

def check_win(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
