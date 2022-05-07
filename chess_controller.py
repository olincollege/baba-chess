"""
Chess Game Controller.
"""
from abc import ABC, abstractmethod

class ChessController(ABC):
    """
    The Chess abstracted class representing the controllers for the Chess game.
    """

    def __init__(self, board):
        """
        Initializes the Chess Board controller, which takes an instance of the
        Chess board as a parameter, and stores it as a private instance
        attribute.
        """
        self._board = board

    @property
    def board(self):
        """
        Returns the Chess board stores in the Chess board instance.
        """
        return self._board

    @abstractmethod
    def move(self):
        """
        A move method that is an abstract method. Used to control the input to
        the Chess game.
        """

class TextController(ChessController):
    """
    The Chess controller that takes in player input and feeds it to the Chess
    game. Takes place of the abstracted move class.
    """

    def move(self):
        """
        Takes in a player input based on the spaces avaliable on the Chess
        board. The player input has to be both the start position and end
        position of the moves.
        """

        try:
            input_number = input("Input move, ie 'e2-e4': ")
            # If the move inputted by the player is "quit", the game is over.
            if input_number == "quit" or input_number == "undo":
                return input_number
            coordinate_tuples = self.lan_to_coords((input_number))
            self._board.move_piece(coordinate_tuples[0], coordinate_tuples[1])
        except (ValueError, KeyError, IndexError):
            print(f"Error: '{input_number}' is not a valid move. "
                    "Input a new move.")
            return "Invalid Move"

    def lan_to_coords(self, lan_input):
        """
        Takes the player's algebraic notation input and translates it to tuple
        form for the ChessBoard class to use.

        Args:
            lan_input: A string representing a chess long-algebraic-notation
                player input.
        
        Returns:
            Returns a tuple of tuples representing the coordinates for the start
            and end coordinates for the ChessBoard class to implement. 
        """
        # first dict is files, second is ranks
        translation_dicts = self._translate_coords()
        translate_ranks = translation_dicts[1]
        translate_files = translation_dicts[0]
        # Parse inputs to translate
        lan_inputs = [i for i in lan_input.split("-")]
        # Assign start and end positions from inputs
        lan_start = lan_inputs[0]
        lan_end = lan_inputs[1]
        return ((translate_ranks[int(lan_start[1])],\
                 translate_files[lan_start[0]]),\
                (translate_ranks[int(lan_end[1])],\
                 translate_files[lan_end[0]]))

    def _translate_coords(self):
        """
        Initializes the dictionaries to be used in order to translate the
        player input from long algebraic notation (LAN) to tuple form.

        Returns:
        Returns a list of dictionaries representing the translation dictionaries
            to be used as a helper for the lan_to_coords method.
        """
        # Generate the translation dictionaries
        files = "abcdefgh"
        translate_files = {}
        translate_ranks = {}
        for i in range(8):
            translate_files[files[i]] = i
            translate_ranks[8-i] = i

        return [translate_files,translate_ranks]
