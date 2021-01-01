import logging


logging.basicConfig(level=logging.DEBUG)


def list_of_empty_lists():
    return [[], [], [], [], [], [], [], [], []]


def empty_3_by_3_matrix():
    return [
        [
            [], [], [],
        ],
        [
            [], [], [],
        ],
        [
            [], [], [],
        ],
    ]


def print_board(board):
    for row_num in range(9):
        print(board[row_num * 9:row_num * 9 + 9])


def row_string(board, row_num):
    return board[row_num * 9:row_num * 9 + 9]


def col_string(board, col_num):
    result = ''
    for row_num in range(9):
        row = row_string(board, row_num)
        result += row[col_num]
    return result


def square_string(board, row_num, col_num):
    start_row_num = int(row_num / 3) * 3
    start_col_num = int(col_num / 3) * 3
    result = ''
    for row_num in range(start_row_num, start_row_num+3):
        row = row_string(board, row_num)
        result += row[start_col_num:start_col_num+3]
    return result


def row_iter(row_num):
    for col_num in range(9):
        yield row_num, col_num


def col_iter(col_num):
    for row_num in range(9):
        yield row_num, col_num


def square_iter(row_num, col_num):
    start_row_num = int(row_num / 3) * 3
    start_col_num = int(col_num / 3) * 3
    for row_num in range(start_row_num, start_row_num+3):
        for col_num in range(start_col_num, start_col_num+3):
            yield row_num, col_num


def possibilities(board, row_num, col_num):
    result = ''
    if cell(board, row_num, col_num) == '.':
        for num in '123456789':
            row = row_string(board, row_num)
            col = col_string(board, col_num)
            square = square_string(board, row_num, col_num)
            if num not in row and num not in col and num not in square:
                result += num
    return result


def cell(board, row_num, col_num):
    row = row_string(board, row_num)
    return row[col_num]


def find_one_possibility(board):
    for row_num in range(9):
        for col_num in range(9):
            if cell(board, row_num, col_num) == '.':
                poss_list = possibilities(board, row_num, col_num)
                if len(poss_list) == 1:
                    return row_num, col_num, poss_list[0]
    # no one-possibility findings
    return None, None, None


def board_set(board, row_num, col_num, number):
    index = row_num*9 + col_num
    newboard = board[0:index] + number + board[index+1:]
    return newboard


def find_hint_one_possibility(board):
    row_num, col_num, number = find_one_possibility(board)
    if row_num is not None:
        return board_set(board, row_num, col_num, number)
    else:
        return None


def iters_all_rows_cols_squares():
    for row_num in range(9):
        logging.debug('iters_all_rows_cols_squares row {}'.format(row_num))
        yield row_iter(row_num)
    for col_num in range(9):
        logging.debug('iters_all_rows_cols_squares col {}'.format(col_num))
        yield col_iter(col_num)
    square_coords = [
        (0, 0), (3, 0), (6, 0),
        (0, 3), (3, 3), (6, 3),
        (0, 6), (3, 6), (6, 6)
    ]
    for row_num, col_num in square_coords:
        logging.debug(
            'iters_all_rows_cols_squares square {} {}'.format(row_num, col_num)
        )
        yield square_iter(row_num, col_num)


def get_poss_lists(board, iter):
    poss_lists = []
    poss_values = set()
    for row_num, col_num in iter:

        # get the list of possible values for this cell if empty
        poss_list = possibilities(board, row_num, col_num)

        # build a set of unique values that could go in cells in this list
        for value in poss_list:
            poss_values.add(value)

        # append a tuple of coordinates and list of possibilities
        poss_lists.append((row_num, col_num, poss_list))

    return poss_lists, poss_values


def find_hint(board):
    # separately consider each row, column, and square
    for iter in iters_all_rows_cols_squares():
        # process one row, column, or square
        result = None
        poss_lists, poss_values = get_poss_lists(board, iter)

        # find a value that can go in exactly one cell
        for value in poss_values:
            value_possible_position_count = 0
            for row_num, col_num, poss_list in poss_lists:
                if value in poss_list:
                    value_possible_position_count += 1
            if value_possible_position_count == 1:
                # we have found a value that can only fit in one row,
                # column, or square
                result = board_set(board, row_num, col_num, value)
                # mission accomplished, just return the one hint and be done
                break  # out of value loop
            if value_possible_position_count > 1:
                # stop considering this value; we don't know where it's going
                break  # out of value loop

        if result is not None:
            break  # out of iter loop

    return result


def solve1(board):
    result = [board]
    while True:
        next_board = find_hint_one_possibility(board)
        if next_board is None or next_board == board:
            break
        board = next_board
        result.append(board)
    return result


def solve(board):
    result = [board]
    while True:
        next_board = find_hint(board)
        if next_board is None or next_board == board:
            break
        board = next_board
        result.append(board)
    return result
