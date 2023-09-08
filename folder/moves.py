from pieces.piece import *
from pieces.bishop import *
from pieces.king import *
from pieces.knight import *
from pieces.pawn import *
from pieces.rook import *
from pieces.queen import *

from typing import List

def get_available_moves(board : List[int], player_color : int) -> List[int]:
    available_moves = []

    for index in range(len(board)) :
        square = board[index]
        if square == 0 : continue
        
        piece = square

        if not is_oponent_piece(piece, player_color) : continue

        available_moves.append(get_piece_moves(index, piece, board))

    return available_moves

def get_piece_moves(index : int, piece : int, board : List[int]) -> List[int] :
    # We don't care if the piece is black or white when calling the get_moves_function
    normalised_piece = piece & 0b0111

    if normalised_piece == 1:
        return get_pawn_moves(index, piece, board)
    elif normalised_piece == 6:
        return get_knight_moves(index, piece, board)
    elif normalised_piece == 5:
        return get_queen_moves(index, piece, board)
    elif normalised_piece == 4:
        return get_rook_moves(index, piece, board)

    match normalised_piece:
        case 3:
            return get_bishop_moves(index, piece, board)
        case 2:
            return get_knight_moves(index, piece, board)