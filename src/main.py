import argparse
import hinter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("print")
    args = parser.parse_args()
    board = args.print
    hinter.print_board(board)
