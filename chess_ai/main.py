"""
    A Classical 8x8 Chess Game (with simplified rules)
    - Character-based pieces
    - No sophisticated moves (castling, en passant, promotion, etc.)
    - Game ends when kind is captured.
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
