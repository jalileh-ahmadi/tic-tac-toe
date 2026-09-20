import random
from itertools import product

def print_board(board):
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i < 2:
            print("--------")

def check_winner(board):
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
        for row in board:
            for cell in row:
                if cell not in ['X', 'O']:
                    return None
    return 'equal'


def get_row_column(number):
    row = (number - 1) // 3
    col = (number - 1) % 3
    return row, col

def get_player_move(board):
    while True:
        try:
            move = int(input('Please enter a number between 1 and 9'))
            if not (1 <= move <= 9):
                print('Invalid input! Please enter a number between 1 and 9')
                continue
            row, col = get_row_column(move)
            if board[row][col] in ['X', 'O']:
                print('that cell is already taken ,choose another')
                continue
            board[row][col] = 'X'
            break
        except ValueError:
            print('Invalid input! Please enter a number.')
            continue

def get_comp_move(board):
    comp_move = random.randint(1, 9)
    row, col = get_row_column(comp_move)
    while board[row][col] in ['X', 'O']:
        comp_move = random.randint(1, 9)
        row, col = get_row_column(comp_move)
    board[row][col] = 'O'

def tic_tac_toe():

    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print_board(board)

    while True:
        get_player_move(board)
        check = check_winner(board)
        if check == True:
            print('you won')
            break
        if check == 'equal':
            print('it is a draw')
            break
        get_comp_move(board)
        print_board(board)
        check = check_winner(board)
        if check == True:
            print('you won')
            break
        elif check == False:
            print('You lost.')
            break
        if check == 'equal':
            print('it is a draw')
            break
        else:
            continue

if __name__ == '__main__':
    tic_tac_toe()