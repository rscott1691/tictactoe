def print_board(board):
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0][0], board[0][1], board[0][2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[1][0], board[1][1], board[1][2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[2][0], board[2][1], board[2][2]))
    print("   |   |   ")

def get_move(player):
    while True:
        try:
            move = int(input("Player {}, enter your move (1-9): ".format(player)))
            if move < 1 or move > 9:
                raise ValueError()
            row = (move - 1) // 3
            col = (move - 1) % 3
            return row, col
        except ValueError:
            print("Invalid move. Please enter a number between 1 and 9.")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    while True:
        print_board(board)
        row, col = get_move(player)
        if board[row][col] != " ":
            print("That space is already taken. Please try again.")
            continue
        board[row][col] = player
        winner = check_win(board)
        if winner:
            print_board(board)
            print("Congratulations, player {} wins!".format(winner))
            return
        if all([space != " " for row in board for space in row]):
            print_board(board)
            print("The game is a draw.")
            return
        player = "O" if player == "X" else "X"

play_game()
