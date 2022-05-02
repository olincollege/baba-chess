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
        coordinates = []
        try:
            input_number = input("Choose the piece you'd like to move and your "
                                "end location(row_start column_start, row_end "
                                "column_end):")
            # If the move inputted by the player is "quit", the game is over.
            if input_number == "quit" or input_number == "undo":
                return input_number
            coordinate_tuples = self.lan_to_coords((input_number))
            self._board.move_piece(coordinate_tuples[0], coordinate_tuples[1])
        except (ValueError, KeyError):
            print(f"Error: '{input_number}' is not a valid move")
            self.move()

    def lan_to_coords(self, lan_input):
        """
        
        """
        #generate the translation dictionaries
        files = "abcdefgh"
        translate_files = {}
        translate_ranks = {}
        for i in range(8):
            translate_files[files[i]] = i
            translate_ranks[8-i] = i
        #parse inputs to translate
        lan_inputs = [i for i in lan_input.split(", ")]
        #assign start and end positions from inputs
        lan_start = lan_inputs[0]
        lan_end = lan_inputs[1]
        return ((translate_ranks[int(lan_start[1])],\
                 translate_files[lan_start[0]]),\
                (translate_ranks[int(lan_end[1])],\
                 translate_files[lan_end[0]]))
        
        
