from typing import List
from pieces.piece import *

def get_knight_moves(index : int, piece : int, board : List[int]) -> List[int]:
    available_moves = [index, piece]

    # Lookup table for knight move offsets
    knight_offsets = [-17, -15, -10, -6, 6, 10, 15, 17]

    for offset in knight_offsets:
        target_index = index + offset
        if 0 <= target_index < 64:
            target_piece = board[target_index]
            if target_piece == 0 or is_oponent_piece(piece, target_piece):
                available_moves.append(target_index)

    return available_moves