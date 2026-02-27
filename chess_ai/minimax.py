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
        if not board.is_black_turn():
            return None  # Minimax is designed for black (AI) to move
        
        best_score = float("-inf")
        best_move: Optional[Move] = None

        move_generator = MoveGenerator(board)
        moves = move_generator.generate_all_moves()

        if not moves:
            return None  # No moves available, game over

        for move in moves:
            board.make_move(move)

            score = self._minimax(board, depth=1)

            board.undo_move()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move
    
    # Core Minimax logic
    def _minimax(self, board: Board, depth: int) -> int:
        """ Recursive minimax search """

        # terminal condition
        if depth == self.max_depth or board.is_game_over():
            evaluator = Evaluator(board)
            return evaluator.evaluate()



