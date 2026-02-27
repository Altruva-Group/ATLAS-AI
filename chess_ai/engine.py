""" 
    Chess Engine
    - Owns board state
    - Implements Minimax algorithm for decision making
    - AI automatically plays Black
    - Human plays White
    - No UI logic inside this class, purely game logic and AI decision making
"""

from typing import Optional, Tuple
from board import Board, Move
from minimax import Minimax
from move_generator import MoveGenerator

class ChessEngine:
    """ Main Chess Engine Class """

    def __init__(self, depth: int = 3) -> None:
        self.board = Board()
        self.ai = Minimax(depth=depth)

    # Public API
    def get_board(self) -> Board:
        """ Return the current board state """
        return self.board
    
    def is_game_over(self) -> bool:
        """ Check if the game is over """
        return self.board.is_game_over()
    
    def print_board(self) -> None:
        """ Print the current board state """
        return self.board.print_board()