"""
    A Classical 8x8 Chess Game (with simplified rules)
    - Character-based pieces
    - No sophisticated moves (castling, en passant, promotion, etc.)
    - Game ends when kind is captured.
    - White (Uppercase) - Human
    - Black (Lowercase) - AI
"""

from engine import ChessEngine


def main() -> None:
    """
    Main function to run the chess game
    """

    print("Welcome to the ATLAS AI!")
    print("This is the Classical AI Chapter's Production Agent")
    print("")

    print("================================")
    print("       Starting New Game")
    print("================================")

    engine = ChessEngine(depth=3)  # You can adjust depth for stronger/weaker AI

    # print board at the initial startup
    print(engine.print_board())

    print("================================")
    print(" Game Over! Thanks for playing.")
    print("================================")


if __name__ == "__main__":
    main()
