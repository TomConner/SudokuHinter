import hinter

BOARD1 = (
    '46.1..5..'
    '..7....12'
    '....84.6.'
    '.2.8....3'
    '3...4...9'
    '9....6.2.'
    '.7.91....'
    '58....2..'
    '..9..5.81'
    )

BOARD2 = (
    '46.1..5..'
    '.97....12'
    '....84.6.'
    '.2.8....3'
    '3...4...9'
    '9....6.2.'
    '.7.91....'
    '58....2..'
    '..9..5.81'
    )

BOARD3 = (
    '46.1..5..'
    '8.7....12'
    '....84.6.'
    '.2.8....3'
    '3...4...9'
    '9....6.2.'
    '.7.91....'
    '58....2..'
    '..9..5.81'
    )


def test_row_string():
    assert hinter.row_string(BOARD1, 1) == '..7....12'


def test_col_string():
    assert hinter.col_string(BOARD1, 2) == '.7......9'


def test_square_string_00():
    assert hinter.square_string(BOARD1, 0, 0) == '46...7...'


def test_square_string_22():
    assert hinter.square_string(BOARD1, 2, 2) == '46...7...'


def test_square_string_34():
    assert hinter.square_string(BOARD1, 3, 4) == '8...4...6'


def test_possibilities_34():
    assert hinter.possibilities(BOARD1, 3, 4) == '579'


def test_find_one_possibility():
    assert hinter.find_one_possibility(BOARD1) == (1, 0, '8')


def test_board_set():
    assert hinter.board_set(BOARD1, 1, 1, '9') == BOARD2


def test_find_hint_one_possibility():
    assert hinter.find_hint_one_possibility(BOARD1) == BOARD3


def test_row_iter():
    result = [(r, c) for r, c in hinter.row_iter(0)]
    assert result == [
        (0, 0), (0, 1), (0, 2),
        (0, 3), (0, 4), (0, 5),
        (0, 6), (0, 7), (0, 8),
    ]


def test_col_iter():
    result = [(r, c) for r, c in hinter.col_iter(4)]
    assert result == [
        (0, 4), (1, 4), (2, 4),
        (3, 4), (4, 4), (5, 4),
        (6, 4), (7, 4), (8, 4),
    ]


def test_square_iter_43():
    result = [(r, c) for r, c in hinter.square_iter(4, 3)]
    assert result == [
        (3, 3), (3, 4), (3, 5),
        (4, 3), (4, 4), (4, 5),
        (5, 3), (5, 4), (5, 5),
    ]


def test_square_iter_88():
    result = [(r, c) for r, c in hinter.square_iter(8, 8)]
    assert result == [
        (6, 6), (6, 7), (6, 8),
        (7, 6), (7, 7), (7, 8),
        (8, 6), (8, 7), (8, 8),
    ]


def test_iters_all_rows_cols_squares():
    all_lists = []

    for iter in hinter.iters_all_rows_cols_squares():
        coord_list = [(row_num, col_num) for row_num, col_num in iter]
        all_lists.append(coord_list)

    # row iters are 0-8
    # list 2 is row 2
    assert all_lists[2] == [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)
    ]

    # col iters are 9-17
    # list 11 is col 2
    assert all_lists[11] == [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)
    ]

    # square iters are 18-26
    # list 18 is upper left square (0,0 through 2,2)
    assert all_lists[18] == [
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
    ]

    # square iters are 18-26
    # list 22 is middle square (3,3 through 5,5)
    assert all_lists[22] == [
        (3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)
    ]
