"""
    A Classical 8x8 Chess Board playing AI.
"""

from board import Board


def main() -> None:
    """
    Main function to run the chess game
    """

    board = Board()

    print("Welcome to the ATLAS AI!")
    print("This is the Classical AI Chapter's Production Agent")
    print(""*3)

    print("----------------")
    print("Starting New Game")
    print("----------------")

    print(board.board)


if __name__ == "__main__":
    main()
