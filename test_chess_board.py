"""
Unit tests for Chess Board
"""
import pytest
from chess_board import ChessBoard, get_piece_color


@pytest.fixture
def board():
    """
    Create a chess board for use in testing.
    """
    return ChessBoard()

board_moves = [
    # Ruy Lopez Opening (Pawn, Bishop, Knight)
    ([((6,4),(4,4)),((1,4),(3,4)),((7,6),(5,5)),((0,1),(2,2)),((7,5),(3,1))],
     [("P"," "),("p"," "),("N"," "),("n"," "),("B"," ")],
     [("white","blank"),("black","blank"),("white","blank"),("black","blank"),
      ("white","blank")]),
    # Queens Gambit Accepted (single capture)
    ([((6,3),(4,3)),((1,3),(3,3)),((6,2),(4,2)),((3,3),(4,2))],
     [("P"," "),("p"," "),("P"," "),("p","P")],
     [("white","blank"),("black","blank"),("white","blank"),("black","white")]),
    # Stafford Gambit Accepted (multiple captures)
    ([((6,4),(4,4)),((1,4),(3,4)),((7,6),(5,5)),((0,6),(2,5)),((5,5),(3,4)),
      ((0,1),(2,2)),((3,4),(2,2)),((1,3),(2,2))],
     [("P"," "),("p"," "),("N"," "),("n"," "),("N","p"),("n"," "),("N","n"),
      ("p","N")],
     [("white","blank"),("black","blank"),("white","blank"),("black","blank"),
      ("white","black"),("black","blank"),("white","black"),("black","white")]),
    # Scandinavian Opening (Queen)
     ([((6,4),(4,4)),((1,3),(3,3)),((4,4),(3,3)),((0,3),(3,3))],
      [("P"," "),("p"," "),("P","p"),("q","P")],
      [("white","blank"),("black","blank"),("white","black"),("black","white")]),
    # Bongcloud (King)
    ([((6,4),(4,4)),((1,4),(3,4)),((7,4),(6,4))],
     [("P"," "),("p"," "),("K"," ")],
     [("white","blank"),("black","blank"),("white","blank")]),
    # Ware Opening (Crab Rooks Variation)
    ([((6,0),(4,0)),((1,4),(3,4)),((7,0),(5,0))],
     [("P"," "),("p"," "),("R"," ")],
     [("white","blank"),("black","blank"),("white","blank")]),
]

invalid_moves = [
    # *Invalid King Moves*
    # King Moves First (self capture)
    ([((7,4),(7,5))]),
    # King Moves more than one square
    ([((6,4),(4,4)),((1,4),(3,4)),((7,4),(5,4))]),
    # *Invalid Queen Moves*
    # Queen Moves First (self capture)
    ([((7,3),(7,2))]),
    # Queen Moves First (Jumps pieces)
    ([((7,3),(4,3))]),
    # Queen Moves to illegal square (L)
    ([((6,3),(4,3)),((1,3),(3,3)),((7,3),(5,3)),((0,3),(2,3)),((5,3),(4,5))]),
    # *Invalid Rook Moves*
    # Rook Moves First (self capture)
    ([((7,0),(7,1))]),
    # Rook Moves First (jumps pieces)
    ([((7,0),(5,0))]),
    # Rook Moves to illegal square (diagonal)
    ([((6,0),(4,0)),((1,4),(3,4)),((7,0),(5,0)),((1,3),(3,3)),((5,0),(4,1))]),
    # *Invalid Bishop Moves*
    # Bishop Moves First (self capture)
    ([((7,5),(6,4))]),
    # Bishop Moves First (jumps pieces)
    ([((7,5),(4,3))]),
    # Bishop Moves to illegal square (horizontal)
    ([((6,3),(4,3)),((1,4),(3,4)),((7,2),(3,6)),((3,4),(4,3)),((3,6),(3,2))]),
    # *Invalid Knight Moves*
    # Knight Self Capture
    ([((7,6),(6,4))]),
    # Knight Moves to illegal square (vertical)
    ([((6,6),(4,6)),((1,4),(3,4)),((7,6),(5,6))]),
    # *Invalid Pawn Moves*
    # Moves more than 2 at start
    ([((6,3),(4,3)),((1,4),(4,4))]),
    # Moves more than 1 after being moved
    ([((6,3),(5,3)),((1,4),(3,4)),((5,3),(3,3))]),
    # Moves diagonally without capture
    ([((6,3),(5,3)),((1,4),(3,4)),((5,3),(4,4))]),
    # Moves backward
    ([((6,4),(4,4)),((1,3),(3,3)),((4,4),(5,4))]),
]

@pytest.fixture(params=board_moves)
def game(request):
    """
    Create a sequence of moves representing a game for use in testing.
    """
    return request.param

@pytest.fixture(params=invalid_moves)
def bad_game(request):
    """
    Create a sequence of moves representing a game for use in testing.
    """
    return request.param

board_reprs = [
    # Ruy Lopez Opening
    ([((6,4),(4,4)),((1,4),(3,4)),((7,6),(5,5)),((0,1),(2,2)),((7,5),(3,1))],
     "   a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r| |b|q|k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p|p| |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | |n| | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | |B| | |p| | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | |P| | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | |N| | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P| |P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q|K| | |R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h"),
    # Queens Gambit Accepted (capture)
    ([((6,3),(4,3)),((1,3),(3,3)),((6,2),(4,2)),((3,3),(4,2))],
     "   a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r|n|b|q|k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p| |p|p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | | | | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | | | | | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | |p|P| | | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P| | |P|P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q|K|B|N|R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h"),
    # Stafford Gambit Accepted (multiple captures)
    ([((6,4),(4,4)),((1,4),(3,4)),((7,6),(5,5)),((0,6),(2,5)),((5,5),(3,4)),
      ((0,1),(2,2)),((3,4),(2,2)),((1,3),(2,2))],
     "   a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r| |b|q|k|b| |r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p| | |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | |p| | |n| | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | | | | | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | |P| | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P| |P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q|K|B| |R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h"),
    # Scandinavian Opening (Queen)
     ([((6,4),(4,4)),((1,3),(3,3)),((4,4),(3,3)),((0,3),(3,3))],
      "   a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r|n|b| |k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p| |p|p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | | | | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | |q| | | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | | | | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P| |P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q|K|B|N|R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h"),
    # Bongcloud (King)
    ([((6,4),(4,4)),((1,4),(3,4)),((7,4),(6,4))],
     "   a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r|n|b|q|k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p|p| |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | | | | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | | |p| | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 | | | | |P| | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 | | | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 |P|P|P|P|K|P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 |R|N|B|Q| |B|N|R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h"),
    # Ware Opening (Crab Rooks Variation)
    ([((6,0),(4,0)),((1,4),(3,4)),((7,0),(5,0))],
     "   a b c d e f g h\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "8 |r|n|b|q|k|b|n|r| 8\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "7 |p|p|p|p| |p|p|p| 7\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "6 | | | | | | | | | 6\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "5 | | | | |p| | | | 5\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "4 |P| | | | | | | | 4\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "3 |R| | | | | | | | 3\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "2 | |P|P|P|P|P|P|P| 2\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "1 | |N|B|Q|K|B|N|R| 1\n"
     "  +-+-+-+-+-+-+-+-+\n"
     "   a b c d e f g h"),
]

@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param

def test_first_move(board):  # pylint: disable=redefined-outer-name
    """
    Test that the first player to move is white.
    Args:
        board: The ChessBoard instance to use.
    """
    assert board.next_player() == "white"

def test_next_player(board, game):  # pylint: disable=redefined-outer-name
    """
    Test that the board correctly selects the next player to move.
    Args:
        board: ChessBoard instance to use.
        game: A tuple whose first element is a list of moves to be made in the
            game, in order.
    """
    moves,_,_ = game
    players = ["white", "black"]
    for i in range(len(moves)):  # pylint: disable=consider-using-enumerate
        assert board.next_player() == players[i % 2]
        board.move_piece(*moves[i])

def test_get_piece(board, game): # pylint: disable=redefined-outer-name
    """
    Test that the board correctly identifies the piece in a square
    Args:
        board: ChessBoard instance to use.
        game: A tuple whose first element is a list of moves to be made in the
            game, in order. The second element is a list of pieces that the
            moves interact with.
    """
    moves,pieces,_ = game
    for i in range(len(moves)): # pylint: disable=consider-using-enumerate
        assert board.get_piece(moves[i][0]) == pieces[i][0]
        assert board.get_piece(moves[i][1]) == pieces[i][1]
        board.move_piece(*moves[i])

def test_get_piece_color(board, game): # pylint: disable=redefined-outer-name
    """
    Test that the board correctly identifies the piece in a square, and that it
    returns "white" for a white piece (uppercase letter), "black" for a black
    piece (lowercase letter), and "blank" for a blank space.
    Args:
        board: ChessBoard instance to use.
        game: A tuple whose first element is a list of moves to be made in the
            game, in order. The second element is a list of pieces that the
            moves interact with.
    """
    moves,_,colors = game
    for i in range(len(moves)): # pylint: disable=consider-using-enumerate
        assert get_piece_color(board.get_piece(moves[i][0])) == colors[i][0]
        assert get_piece_color(board.get_piece(moves[i][1])) == colors[i][1]
        board.move_piece(*moves[i])

def test_invalid_games(board, bad_game): # pylint: disable=redefined-outer-name
    """
    Test that invalid moves raise ValueError.
    Args:
        board: ChessBoard instance to use.
        bad_game: A list of tuples that represent invalid moves that should
            raise a ValueError due to either capturing its own color or moving
            in a way it shouldn't.
    """
    moves = bad_game
    for i in range(len(moves)-1):
        board.move_piece(*moves[i])
    with pytest.raises(ValueError):
        board.move_piece(*moves[-1])

def test_undo_move(board, game_repr): # pylint: disable=redefined-outer-name
    """
    Test that undoing a move properly restores the board to the state before the
    move undone.
    Args:
        board: ChessBoard instance to use.
        game: A tuple whose first element is a list of moves to be made in the
            game, in order. The second element is a list of pieces that the
            moves interact with.
    """
    moves, board_repr = game_repr
    for start, end in moves:  # pylint: disable=redefined-outer-name
        board.move_piece(start, end)
    if board.next_player() == "black":
        board.move_piece((1,0),(2,0)) # a move to be undone
    else:
        board.move_piece((6,7),(5,7)) # a move to be undone
    board.undo_move()
    assert str(board) == board_repr

def test_repr(board, game_repr):  # pylint: disable=redefined-outer-name
    """
    Test that the board is correctly represented as a string in different
    conditions.
    Args:
        board: The ChessBoard instance to use.
        game_repr: A tuple where the first element is a list of moves to be made
            in the game, and the second element is a string representing the
            expected string representation of the board after those moves have
            been made.
    """
    moves, board_repr = game_repr
    for start, end in moves:  # pylint: disable=redefined-outer-name
        board.move_piece(start, end)
    assert str(board) == board_repr
