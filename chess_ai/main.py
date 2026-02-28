"""
    A Classical 8x8 Chess Game (with simplified rules)
    - Character-based pieces
    - No sophisticated moves (castling, en passant, promotion, etc.)
    - Game ends when kind is captured.
    - White (Uppercase) - Human
    - Black (Lowercase) - AI
"""

from cli import ChessCLI


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

    cli = ChessCLI(depth=3)  # Adjust depth for stronger/weaker AI

    cli.start()

    print("================================")
    print(" Game Over! Thanks for playing.")
    print("================================")


if __name__ == "__main__":
    main()
