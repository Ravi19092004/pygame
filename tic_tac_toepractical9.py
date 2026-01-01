def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return True
    
    return False

def main():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        
        move = input(f"Player {current_player}, enter your move (1-9): ")
        
        if board[int(move) - 1] == " ":
            board[int(move) - 1] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif " " not in board:
                print_board(board)
                print("It's a tie!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    main()

