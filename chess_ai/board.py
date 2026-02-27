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

    # Board Utility Methods
    def is_within_bounds(self, row: int, col: int) -> bool:
        """ Check if a position is within the board boundaries """
        return 0 <= row < 8 and 0 <= col < 8
    
    def get_piece(self, position: Position) -> str: 
        """ Get the piece at a given position """
        row, col = position
        if self.is_within_bounds(row, col):
            return self.board[row][col]
        return None  # Out of bounds
    
    def set_piece(self, position: Position, piece: str) -> None:
        """ Set a piece at a given position """
        row, col = position
        if self.is_within_bounds(row, col):
            self.board[row][col] = piece

    def clone(self) -> 'Board':
        """ Create a deep copy of the board """
        new_board = Board()
        new_board.board = deepcopy(self.board)
        new_board.turn = self.turn
        new_board.white_king_pos = self.white_king_pos
        new_board.black_king_pos = self.black_king_pos
        new_board.move_history = deepcopy(self.move_history)
        return new_board
    
    # move execution
    def make_move(self, move: Move) -> Optional[str]:
        """ Execute a move on the board and return any captured piece """
        (from_row, from_col), (to_row, to_col) = move

        piece = self.get_piece((from_row, from_col))
        captured_piece = self.get_piece((to_row, to_col))

        # Move the piece
        self.set_piece((to_row, to_col), piece)
        self.set_piece((from_row, from_col), ".")

        # Update king position if needed
        if piece == "K":
            self.white_king_pos = (to_row, to_col)
        elif piece == "k":
            self.black_king_pos = (to_row, to_col)

        # Record move history
        self.move_history.append((move, captured_piece))

        # Switch turn
        self._switch_turn()

        return captured_piece if captured_piece != "." else None
    
    def undo_move(self) -> None:
        """ Undo the last move made on the board """
        if not self.move_history:
            return  # No moves to undo

        last_move, captured_piece = self.move_history.pop()
        (from_row, from_col), (to_row, to_col) = last_move

        moved_piece = self.get_piece((to_row, to_col))

        # Move the piece back
        self.set_piece((from_row, from_col), moved_piece)

        # Restore captured piece if there was one
        self.set_piece((to_row, to_col), captured_piece if captured_piece else ".")

        # Restore king position if needed
        if moved_piece == "K":
            self.white_king_pos = (from_row, from_col)
        elif moved_piece == "k":
            self.black_king_pos = (from_row, from_col)

        # Switch turn back
        self._switch_turn()

    def _switch_turn(self) -> None:
        """ Switch the current player's turn """
        self.turn = "black" if self.turn == "white" else "white"


    # Game State Evaluation
    def is_game_over(self) -> bool:
        """ Check if the game is over (king captured) """
        return self.get_piece(self.white_king_pos) == "." or self.get_piece(self.black_king_pos) == "."
    

    # Diplay Methods
    def print_board(self) -> None:
        """ Print the chess board """
        print("\n  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8 - i, " ".join(row), 8 - i)
        print("  a b c d e f g h\n")

    # Turn Helpers
    def get_current_player(self) -> str:
        """ Get the current player's color """
        return self.turn
    
    def is_white_turn(self) -> bool:
        """ Check if it's white's turn """
        return self.turn == "white"
    
    def is_black_turn(self) -> bool:
        """ Check if it's black's turn """
        return self.turn == "black"