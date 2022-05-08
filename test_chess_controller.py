"""
Unit tests for tic-tac-toe controller.
"""
import io
import pytest
from chess_board import ChessBoard
from chess_controller import TextController


@pytest.fixture(name='board')
def chess_board():
    """
    Create a tic tac toe board for use in testing.
    """
    return ChessBoard()


# Test cases for move. Since the prompt repeats until given an valid input, each
# sequence ends with a valid input.
move_cases = [
    # Single valid move.
    ("e2-e4", {(4, 4): "P"}),
    # Multiple valid moves.
    ("e2-e4\nd7-d6", {(4, 4): "P",
                  (2, 3): "p"}),
    # Only one index given.
    ("e2\ne2-e4", {(4, 4): "P"}),
    # Non-numerical input.
    ("0 abc\nabc 0\nabc def\ne2-e4", {(4, 4): "P"}),
    # Row or column index too large.
    ("b2-b9\nb2-b9\np7-p8\ne2-e4", {(4, 4): "P"}),
    # A capture is made on white's 2nd move
    ("e2-e4\nb7-b5\nf1-b5", {(4, 4): "P",
                       (3, 1): ["p", "B"]}),
]

# Define sets of test cases.
translation_cases = [
    # Single valid move.
    ("e2-e4", ((6,4),(4, 4))),
    # Multiple valid moves.
    ("d7-d6", ((1,3),(2, 3))),
    # A capture is made on white's 2nd move
    ("g1-c5", ((7, 6), (3, 2))),
]

@pytest.fixture(name='move_case', params=move_cases)
def chess_move_case(request):
    """
    Provide a pair of text input to the move method of the controller and the
    expected board state.
    """
    return request.param

# @pytest.mark.parametrize("move_case", move_cases)
def test_draw(board, move_case, monkeypatch):
    """
    Test that the board is correctly represented as a string in different
    conditions.

    Args:
        board: The ChessBoard instance to use.
        move_case: A tuple consisting of a string representing input to the move
            method of the TextController instance used, and a dictionary mapping
            (row, col) tuples to the expected mark found there after the input
            has been consumed by the controller (the default mark is assumed to
            be blank).
    """
    controller = TextController(board)
    user_input, check_squares = move_case
    valid_moves = 0
    move_length = 0

    # Patch standard input to pass the text in user_input to the move method.
    monkeypatch.setattr("sys.stdin", io.StringIO(user_input))

    # Consume all input until none is left, using it to make moves in the game.
    try:
        while True:
            move = controller.move()
            if move is None:
                valid_moves += 1
    except (EOFError, ValueError):
        pass

    # Check that the move method was called the appropriate number of times.
    for key in check_squares:
        move_length += len(check_squares[key])
    assert valid_moves == move_length

    # Check that the board contains exactly the correct marks.
    for row in range(8):
        for col in range(8):
            if (row, col) in check_squares:
                if len(check_squares[(row, col)]) != 1:
                    assert board.get_piece((row, col)) == check_squares[(row, col)][-1]
                else:
                    assert board.get_piece((row, col)) == check_squares[(row, col)]
            elif 2 <= row <= 5:
                assert board.get_piece((row, col)) == board.blank_square


@pytest.mark.parametrize("lan,tuples", translation_cases)
def test_lan_to_coords(board, lan, tuples):
    """
    Test that the translation from long-algebraic-notation to tuple form is
    implemented properly

    Args:
        board: The ChessBoard instance to use.
        lan: A string representing the user's long algebraic notation. This will
            translated into tuple form for the other game classes to use.
        tuples: A tuple of tuples representing the translated user input. This
            is implemented within the Model class.
    """
    controller = TextController(board)
    assert controller.lan_to_coords(lan) == tuples
