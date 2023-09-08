from typing import List
from pieces.piece import *

def get_king_moves(index : int, piece : int, board : List[int]) -> List[int]:
    available_moves = [index, piece]

    # King move directions (horizontal, vertical, and diagonal)
    directions = [
        (-1, -1),(-1, 0),(-1, 1),
        ( 0, -1),         (0, 1),
        ( 1, -1),( 1, 0), (1, 1)
    ]

    for dx, dy in directions:
        x, y = index % 8 + dx, index // 8 + dy
        target_index = x + y * 8

        if 0 <= target_index < 64:
            target_piece = board[target_index]
            if target_piece == 0 or is_oponent_piece(piece, target_piece):
                available_moves.append(target_index)

    return available_moves