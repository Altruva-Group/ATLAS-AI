"""
    A Classical 8x8 Chess Board (with simplified rules)
    - Character-based pieces
    - Uppercase = White
    - Lowercase = Black
    - Empty square = '.'
    - No sophisticated moves (castling, en passant, promotion, etc.)
    - Game ends when kind is captured.
"""
from copy import deepcopy
from typing import List, Tuple, Optional

Position = Tuple[int, int]  # (row, col)
Move = Tuple[Position, Position]  # ((from_row, from _col), (to_row, to_col))


class Board:
    """
    A Classical 8x8 Chess Board
    """

    def __init__(self) -> None:
        self.board: List[List[str]] = self._create_initial_board()
        self.turn: str = "white"  # white starts
        self.white_king_pos: Position = (7, 4)
        self.black_king_pos: Position = (0, 4)
        self.move_history: List[Tuple[Move, str]] = []

    def _create_initial_board(self) -> List[List[str]]:
        """
        Create the initial state of the board
        """

        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
