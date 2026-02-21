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
