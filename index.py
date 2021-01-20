import random
from IPython.display import clear_output


def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Choose between X or O: ")
        player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def win_check(board, mark):
    mark_list = [mark, mark, mark]
    if (board[1:4] == mark_list or board[4:7] == mark_list or board[7:10] == mark_list or board[1:8:3] == mark_list or board[2:9:3] == mark_list or board[3:10:3] == mark_list or board[1:10:4] == mark_list or board[3:8:2] == mark_list):
        return True
    else:
        return False


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def place_marker(board, marker, position):
    board[position] = marker


def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    choice = input("Do you want to play again? Enter 'YES' or 'NO': ")
    if choice == 'NO':
        return True
    else:
        return False
    pass
