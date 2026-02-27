"""
    Classical Depth-Limited Minimax
    - No alpha-beta pruning
    - No heuristics beyond static evaluation
    - Black is maximizing player (AI)
    - White is minimizing player (Human)
"""

from typing import Optional, Tuple, List
from board import Board, Move
from move_generator import MoveGenerator
from evaluation import Evaluator

class Minimax:
    """ Implement the Minimax algorithm """
    def __init__(self, depth: int = 3) -> None:
        self.max_depth = depth

    # Public API
    def find_best_move(self, board: Board) -> Optional[Move]:
        """ Find the best move for the current player using Minimax """
