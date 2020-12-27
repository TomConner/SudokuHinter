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
