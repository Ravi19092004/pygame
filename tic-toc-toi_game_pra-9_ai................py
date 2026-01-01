def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

#function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

#function to check for a win
def check_win(board, player):
    #check rows
    for row in board:
        if all(spot == player for spot in row):
            return True
    #check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    #check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False
#function to play Tic-Tac-Toe
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        
        # check if the spot is available
        if board[row][col] != " ":
            print("That spot is already taken, try again.")
            continue
        
        # place the player's mark on the board
        board[row][col] = current_player
        
        # check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # switch players
        current_player = "O" if current_player == "X" else "X"
    
#start the game
if __name__ == "__main__":
    play_game()
