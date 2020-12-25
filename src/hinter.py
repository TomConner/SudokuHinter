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
