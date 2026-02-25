"""
    Move Generator Class
    Simplified rules:
    - No castling
    - No en passant
    - No promotion
    - Pawns move forward, capture diagonally
"""

from typing import List, Tuple
from board import Board, Position, Move


class MoveGenerator:
    """ Generates pseudo-legal moves (ignores check conditions) """

    def __inti__(self, board: Board) -> None:
        self.board = board

    # public API
    def generate_all_moves(self) -> List[Move]:
        """ Generate all moves for the current player """
        moves: List[Move] = []

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]

                if piece == ".":
                    continue # empty square

                if self._belongs_to_current_player(piece):
                    piece_moves = self._generate_piece_moves(piece, row, col)
                    moves.extend(piece_moves)