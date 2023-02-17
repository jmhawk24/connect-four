import numpy as np


def create_board():
    return np.zeros((6, 7), int)


def add_next_piece(col_selection, current_player):
    if is_valid_location(col_selection):
        board[get_next_open_row(col_selection)][col_selection] = current_player


def is_valid_location(selection):
    if board[0][selection] == 0:
        return True
    else:
        return False


def get_next_open_row(col_selection):
    col_vals = []
    for row in board:
        col_vals.append(row[col_selection])

    for i, val in enumerate(col_vals):
        if val > 0:
            return i-1
        elif int(val) == 0 and i == 5:
            return i

    return -1


def horiz_winner(board):
    for row in board:
        for i in range(0, 4):
            this_select = set(row[i:i+4])
            if len(this_select) == 1 and this_select.copy().pop() > 0:
                return int(this_select.pop())

    return 0


def vert_winner(board):
    for i in range(0, 3):
        rows = board[i:i+4]
        for j in range(0, 7):
            col_list = []
            for row in rows:
                col_list.append(row[j])

            if len(set(col_list)) == 1 and set(col_list).copy().pop() > 0:
                return set(col_list).pop()

    return 0


def reverse_board(board):
    reversed_board = list()
    for row in board:
        reversed_board.append(list(row)[::-1])

    return np.array(reversed_board)


def diag_winner(board):
    boards = (board, reverse_board(board))
    for each_board in boards:
        for i in range(-2, 4):
            diag = each_board.diagonal(i)
            for j in range(0, len(diag)-3):
                group_of_four = diag[j:j+4]
                if len(set(group_of_four)) == 1 and set(group_of_four).copy().pop() > 0:
                    return set(group_of_four).pop()

    return 0


def get_winner(board):
    # return 0 if no winner, 1 if player 1, 2 if player 2
    # winner if four in a row horiz, diag, or vert
    return horiz_winner(board) or vert_winner(board) or diag_winner(board)


def col_is_full(board, col_selection):
    return board[0][col_selection] > 0


def is_col_available(board, col_selection):
    if col_is_full(board, col_selection):
        print("The column you picked is full.")
        print("Pick another column.")
        print("---")
        return False
    else:
        return True


def coerce_input(input):
    try:
        coerced_input = int(input)
    except ValueError:
        print("""You didn't enter a valid value.
        Enter an integer between 0 and 6.""")
        return -1

    if coerced_input > 6 or coerced_input < 0:
        print("""You didn't enter a valid value.
                Enter an integer between 0 and 6.""")
        return -1

    return coerced_input


def run_game(turn, board, game_over):
    while not game_over:
        print(board)
        print("  0 1 2 3 4 5 6  ")  # make this dynamic with width of board
        player_going = True
        if turn % 2 == 0:
            while player_going:
                col_selection = coerce_input(input("Player 1, make your selection (0-6)!"))
                if col_selection >= 0 and is_col_available(board, col_selection):
                    add_next_piece(col_selection, 1)
                    player_going = False
        else:
            while player_going:
                col_selection = coerce_input(input("Player 2, make your selection (0-6)!"))
                if col_selection >= 0:
                    add_next_piece(col_selection, 2)
                    player_going = False

        winner = get_winner(board)
        if winner > 0:
            game_over = True
            print(board)
            print("WE HAVE A WINNER! The winner is Player " + str(winner) + " on turn number " + str(turn))

        turn += 1


if __name__ == '__main__':
    turn_counter = 0
    board = create_board()
    game_over = False
    run_game(turn_counter, board, game_over)

# TODO: make the column hint guide dynamic based off size of board?
