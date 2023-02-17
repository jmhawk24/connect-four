# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def create_board():
    return np.zeros((6, 7))


def add_next_piece(col_selection, current_player):
    print(col_selection)
    if is_valid_location(col_selection):
        board[get_next_open_row(col_selection)][col_selection] = current_player


def is_valid_location(selection):
    if board[0][selection] == 0:
        print("we valid!!")
        return True
    else:
        return False


def get_next_open_row(col_selection):
    col_vals = []
    for row in board:
        col_vals.append(row[col_selection])

    for i, val in enumerate(col_vals):
        print(val)
        if val > 0:
            return i-1
        elif int(val) == 0 and i == 5:
            return i

    return -1


def horiz_winner(board):
    #per row, check to see if any 4 sequential entries are all the same
    list = []
    i = 0
    thisSelect = list[i:i+4]
    pass


def vert_winner(board):
    pass


def diag_winner(board):
    pass


def get_winner(board):
    # return 0 if no winner, 1 if player 1, 2 if player 2
    # winner if four in a row horiz, diag, or vert
    return horiz_winner(board) or vert_winner(board) or diag_winner(board)


def run_game(turn, board, game_over):
    while not game_over:
        print(board)

        if turn % 2 == 0:
            col_selection = int(input("Player 1, make your selection (0-6)!"))
            add_next_piece(col_selection, 1)
        else:
            col_selection = int(input("Player 2, make your selection (0-6)!"))
            add_next_piece(col_selection, 2)

        winner = get_winner(board)
        if winner > 0:
            game_over = True

        turn += 1


if __name__ == '__main__':
    turn_counter = 0
    board = create_board()
    game_over = False
    run_game(turn_counter, board, game_over)
