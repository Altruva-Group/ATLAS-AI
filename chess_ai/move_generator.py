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

    def __init__(self, board: Board) -> None:
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

    # Sliding Pieces (Rook, Bishop, Queen)
    def _rook_moves(self, piece: str, row: int, col: int) -> List[Move]:
        """ Generate moves for rook """
        return self._sliding_moves(piece, row, col, directions=[
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ])
    
    def _bishop_moves(self, piece: str, row: int, col: int) -> List[Move]:
        """ Generate moves for bishop """
        return self._sliding_moves(piece, row, col, directions=[
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ])
    
    def _queen_moves(self, piece: str, row: int, col: int) -> List[Move]:
        """ Generate moves for queen """
        return self._sliding_moves(piece, row, col, directions=[
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ])
    
    def _sliding_moves(
        self,
        piece: str,
        row: int,
        col: int,
        directions: List[Tuple[int, int]]
    ) -> List[Move]: 
        """ Generate moves for sliding pieces """
        moves: List[Move] = []

        for d_row, d_col in directions:
            current_row = row + d_row
            current_col = col + d_col

            while self.board.is_within_bounds(current_row, current_col):
                target = self.board.board[current_row][current_col]

                if target == ".":
                    moves.append(((row, col), (current_row, current_col)))
                else:
                    if not self._same_color(piece, target):
                        moves.append(((row, col), (current_row, current_col)))
                    break  # blocked by piece from same player

                current_row += d_row
                current_col += d_col

        return moves
    
    # Knight moves
    def _knight_moves(self, piece: str, row: int, col: int) -> List[Move]:
        """ Generate moves for knight """
        moves: List[Move] = []

        knight_offsets = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        for d_row, d_col in knight_offsets:
            new_row = row + d_row
            new_col = col + d_col

            if self.board.is_within_bounds(new_row, new_col):
                target = self.board.board[new_row][new_col]
                if target == "." or not self._same_color(piece, target):
                    moves.append(((row, col), (new_row, new_col)))

        return moves
    
    # King moves
    def _king_moves(self, piece: str, row: int, col: int) -> List[Move]:
        """ Generate moves for king """
        moves: List[Move] = []

        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                if d_row == 0 and d_col == 0:
                    continue # skip no-move

                new_row = row + d_row
                new_col = col + d_col

                if self.board.is_within_bounds(new_row, new_col):
                    target = self.board.board[new_row][new_col]
                    if target == "." or not self._same_color(piece, target):
                        moves.append(((row, col), (new_row, new_col)))
        
        return moves
    
    # Helpers
    def _belongs_to_current_player(self, piece: str) -> bool:
        """ Check if piece belong to current player """
        if self.board.is_white_turn():
            return piece.isupper()
        return piece.islower()
    
    def _same_color(self, piece1: str, piece2: str) -> bool:
        return (piece1.isupper() and piece2.isupper()) or \
                (piece1.islower() and piece2.islower())

