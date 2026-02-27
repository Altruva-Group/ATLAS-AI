"""
    ATLAS Chess AI - Command Line Interface (CLI)
    - Provides a simple text-based interface to play against the AI.
    - Uses the ChessEngine to manage game state and AI moves.
    - Human player (White) inputs moves in standard algebraic notation (e.g., e2e4).
    - AI player (Black) automatically responds after human move.
    - Input format: "e2e4" (move piece from e2 to e4)
"""

from typing import Optional, Tuple
from engine import ChessEngine
from board import Move


class ChessCLI:
    """ Command Line Interface for the Chess Game """

    def __init__(self, depth: int = 3) -> None:
        self.engine = ChessEngine(depth=depth)

    # Main loop
    def start(self) -> None:
        """ Main loop to run the CLI """

        print("You are White (Uppercase), AI is Black (lowercase).")
        print("Enter moves in format: e2e4 (move piece from e2 to e4)")
        print("Game ends when a king is captured. Good luck!\n")

        while not self.engine.is_game_over():
            print(self.engine.print_board())

            move_input = input("Your move: ").strip()
            parsed_move = self._parse_move(move_input)

            if parsed_move is None:
                print("Invalid move format. Please use format like: e2e4.\n")
                continue

            success = self.engine.make_human_move(parsed_move)

            if not success:
                print("Illegal move. Please try again.\n")
                continue

        # Game over
        self.engine.print_board()
        

    # Parsing user input
    def _parse_move(self, move_str: str) -> Optional[Move]:
        """ Converts user inputs like e2e4 to ((6, 4), (4, 4)) """

        if len(move_str) != 4:
            return None

        from_sq = move_str[:2]
        to_sq = move_str[2:]

        from_pos = self._algebraic_to_index(from_sq)
        to_pos = self._algebraic_to_index(to_sq)

        if from_pos is None or to_pos is None:
            return None
        
        return (from_pos, to_pos)
    
    def _algebraic_to_index(self, sq: str) -> Optional[Tuple[int, int]]:
        """ 
            Converts algebraic notation (e.g., e2) to board indices (row, col)
            Example:
            e2 -> (6, 4)  # row 6 (rank 2), col 4 (file e)
        """


