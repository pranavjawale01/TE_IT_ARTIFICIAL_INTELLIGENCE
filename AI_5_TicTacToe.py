def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)
        
def check_wineer(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False 
    return True

if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]
    curr_player = "x"
    
    while True:
        print_board(board)
        print(f"Player {curr_player}'s turn ")
        
        row = int(input("Enter row (0, 1, 2) : "))
        col = int(input("Enter col (0, 1, 2) : "))
        
        if board[row][col] != " ":
            print("The cell is already filled")
            continue
        
        board[row][col] = curr_player
        
        winner = check_wineer(board)
        
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a Tie")
            break
        
        curr_player = "o" if curr_player == 'x' else 'x'
        
 