"""
    Evaluation Function
    - Positive score favors Black (AI).
    - Negative score favors White (Human).
    - No positional heuristics.
    - No dynamic adjustments.
    - Deterministic clasical evaluation based on material count only.
"""

from board import Board


class Evaluator:
    """ Evaluates the board state from the perspective of the AI (Black)"""

    PIECE_VALUES = {
        "p": 1,  # Pawn
        "n": 3,  # Knight
        "b": 3,  # Bishop
        "r": 5,  # Rook
        "q": 9,  # Queen
        "k": 1000   # K: Large value to represent important 
    }

    def __init__(self, board: Board) -> None:
        self.board = board

    def evaluate(self) -> int:
        """ Returns material score of the board. 
            - Black pieces add to score.
            - White pieces subtract from score.        
        """

        score = 0

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]

                if piece == ".":
                    continue  # empty square

                piece_value = self.PIECE_VALUES.get(piece.lower(), 0)

                if piece.islower(): # Black
                    score += piece_value
                else: # White
                    score -= piece_value

        return score