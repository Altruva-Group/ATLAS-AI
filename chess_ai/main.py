"""
    A Classical 8x8 Chess Game (with simplified rules)
    - Character-based pieces
    - No sophisticated moves (castling, en passant, promotion, etc.)
    - Game ends when kind is captured.
"""

from board import Board
from minimax import Minimax


def main() -> None:
    """
    Main function to run the chess game
    """

    board = Board()
    # move_generator = MoveGenerator(board)
    # evaluator = Evaluator(board)

    print("Welcome to the ATLAS AI!")
    print("This is the Classical AI Chapter's Production Agent")
    print("")

    print("================================")
    print("       Starting New Game")
    print("================================")

    print(board.print_board())
    print(board.move_history)

    # print(board.make_move(((6, 4), (4, 4))))  # Move white pawn from e2 to e4 - testing

    print(board.make_move(((1, 4), (3, 4))))  # Move black pawn from e7 to e5 - testing

    # minimax testing
    print("AI is thinking...")
    print(Minimax(depth=3).find_best_move(board))

    print(board.move_history)

    print("================================")
    print(" Game Over! Thanks for playing.")
    print("================================")


if __name__ == "__main__":
    main()
