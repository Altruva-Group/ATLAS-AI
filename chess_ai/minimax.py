"""
    Classical Depth-Limited Minimax
    - No alpha-beta pruning
    - No heuristics beyond static evaluation
    - Black is maximizing player (AI)
    - White is minimizing player (Human)
"""

from typing import List, Tuple, List
from board import Board, Move
from move_generator import MoveGenerator
from evaluation import Evaluator

class Minimax:
    """ Implement the Minimax algorithm """
    def __init__(self, depth: int = 3) -> None:
        self.max_depth = depth