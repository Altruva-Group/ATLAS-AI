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