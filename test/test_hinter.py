import hinter

BOARD1 = (
    '46.1..5....7....12....84.6..2.8....3'
    '3...4...99....6.2..7.91....58....2....9..5.81'
    )


def test_row_string():
    assert hinter.row_string(BOARD1, 1) == '..7....12'

# def test_col_string(self):
#    assertEquals(hinter.col_string(BOARD1, 10), '..7....12')
