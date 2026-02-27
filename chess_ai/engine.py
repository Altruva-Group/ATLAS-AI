""" 
    Chess Engine
    - Owns board state
    - Implements Minimax algorithm for decision making
    - AI automatically plays Black
    - Human plays White
    - No UI logic inside this class, purely game logic and AI decision making
"""

from typing import Optional #, Tuple
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
    
    # Human move (White) handling
    def make_human_move(self, move: Move) -> bool:
        """ 
            Attempt to make a move for the human player (White) 
            Returns:
                - True if move was valid and executed
                - False otherwise
        """

        if not self.board.is_white_turn():
            return False  # Not human's turn
        
        move_generator = MoveGenerator(self.board)
        valid_moves = move_generator.generate_all_moves()

        if move not in valid_moves:
            return False  # Invalid move
        
        self.board.make_move(move)

        # After human move, trigger AI move if game is not over
        if not self.board.is_game_over():
            print("AI is thinking...")
            self._make_ai_move()

        return True
    
    # AI move  (Black) handling
    def _make_ai_move(self) -> Optional[Move]:
        """ 
            Automatically executes AI move if it's Black's turn. 
            Returns:
                - The move made by the AI, or None if no moves available
        """

        if not self.board.is_black_turn():
            return None  # Not AI's turn
        
        best_move = self.ai.find_best_move(self.board)

        if best_move is not None:
            self.board.make_move(best_move)
        
        return best_move
