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

        return moves
    
    # Piece moves
    def _generate_piece_moves(self, piece: str, row: int, col: int) -> List[Move]:
        """ Generate moves for a specific piece """
        piece_type = piece.lower()

        if piece.lower() == "p":
            return self._pawn_moves(piece, row, col)
        elif piece.lower() == "r":
            return self._rook_moves(piece, row, col)
        elif piece.lower() == "n":
            return self._knight_moves(piece, row, col)
        elif piece.lower() == "b":
            return self._bishop_moves(piece, row, col)
        elif piece.lower() == "q":
            return self._queen_moves(piece, row, col)
        elif piece.lower() == "k":
            return self._king_moves(piece, row, col)
        else:
            return []

    # Pawn moves
    def _pawn_moves(self, piece: str, row: int, col: int) -> List[Move]: 
        """ Generate moves for pawn """
        moves: List[Move] = []
        direction = -1 if piece.isupper() else 1  # white moves up, black moves down

        forward_row = row + direction

        # forward move
        if self.board.is_within_bounds(forward_row, col):
            if self.board.board[forward_row][col] == ".":
                moves.append(((row, col), (forward_row, col)))

        # diagonal captures
        for delta_col in [-1, 1]:
            capture_col = col + delta_col
            if self.board.is_within_bounds(forward_row, capture_col):
                target_piece = self.board.board[forward_row][capture_col]
                if target_piece != "." and not self._same_color(piece, target_piece):
                    moves.append(((row, col), (forward_row, capture_col)))

        return moves
