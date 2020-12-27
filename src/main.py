import argparse
import hinter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("board")
    args = parser.parse_args()
    board = args.board
    steps = hinter.solve(board)
    for step in steps:
        hinter.print_board(step)
        print()
