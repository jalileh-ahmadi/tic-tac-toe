import random
board = [['1', '2' , '3'], ['4', '5', '6'], ['7', '8', '9']]
def reset_board():
    global board
    board = [['1', '2' , '3'], ['4', '5', '6'], ['7', '8', '9']]
def printBoard():
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i < 2:
            print("--------")
def winner():
    for row in board:
        if row[0] == row[1] == row[2] == 'X':
            return True
        elif row[0] == row[1] == row[2] == 'O':
            return False
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return True
        elif board[0][i] == board[1][i] == board[2][i] == 'O':
            return False
    if board[0][0] == board[1][1] == board[2][2] == 'X' or  board[0][2] == board[1][1] == board[2][0] == 'X':
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return False
    else:
        return 'equal'
def get_int_input(prompt, valid_range=None):
    while True:
        try:
            value = int(input(prompt))
            if valid_range and value not in valid_range:
                print(f"Please enter a number between {valid_range.start} and {valid_range.stop - 1}.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")
def playing():
    printBoard()
    player = get_int_input("turn X- enter a cell number(1-9)",range(1,10))
    row = (player - 1) // 3
    col = (player - 1) % 3
    while board[row][col] in ['X', 'O']:
        player = get_int_input('that cell is already taken ,choose another' , range(1,10))
        row = (player - 1) // 3
        col = (player - 1) % 3
    print('computer is thinking...')
    board[row][col] = 'X'
    check = winner()
    if check == True:
        print('You win!')
        return True
    elif check == False:
        print('Computer wins!')
        return True
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['X','O']]
    if empty_cells:
        rowc , colc = random.choice(empty_cells)
        board[rowc][colc] = 'O'
    check = winner()
    if check == True:
        print('you win')
        return True
    elif check == False:
        print('computer wins')
        return True
    elif len(empty_cells) == 0 :
        print("It's a draw")
        return True
while True:
    for t in range(9):
        end = playing()
        if end:
            printBoard()
            break
    reset_board()
    tryAgain = input('play again? (y / n)').lower()
    if tryAgain != 'y':
        break
            