# from pprint import pprint


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


def possibilities(board, row_num, col_num):
    result = ''
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
