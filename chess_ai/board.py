"""
    A Classical 8x8 Chess Board
    - Character-based pieces
    - Uppercase = White
    - Lowercase = Black
    - Empty square = '.'
"""
from copy import deepcopy
from typing import List, Tuple, Optional

Position = Tuple[int, int]  # (row, col)
Move = Tuple[Position, Position]  # ((from_row, from _col), (to_row, to_col))


class Board:
    """
     Chess Board Class
    """

    def __init__(self) -> None:
        self.board: List[List[str]] = self._create_initial_board()
        self.turn: str = "white"  # white starts
        self.white_king_pos: Position = (7, 4)  # index 0
        self.black_king_pos: Position = (0, 4)  # index 0
        self.move_history: List[Tuple[Move, str]] = []

    def _create_initial_board(self) -> List[List[str]]:
        """ Create the initial state of the board """

        board = [["." for _ in range(8)] for _ in range(8)]

        # board pieces
        board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]  # black pieces
        board[1] = ["p"] * 8  # black pawns
        board[6] = ["P"] * 8  # white pawns
        board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]  # white pieces

        return board

    def print_board(self) -> None:
        """ Print the chess board """
        print("\n  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8 - i, " ".join(row), i + 1)
        print("  a b c d e f g h\n")
