"""
    ATLAS Chess AI - Command Line Interface (CLI)
    - Provides a simple text-based interface to play against the AI.
    - Uses the ChessEngine to manage game state and AI moves.
    - Human player (White) inputs moves in standard algebraic notation (e.g., e2e4).
    - AI player (Black) automatically responds after human move.
    - Input format: "e2e4" (move piece from e2 to e4)
"""

from typing import Optional, Tuple
from engine import Engine
from board import Move


class ChessCLI:
    """ Command Line INterface for the Chess Game """

    def __init__(self, depth: int = 3) -> None:
        self.engine = Engine(depth=depth)

    # Main loop
    def start(self) -> None:
        print()