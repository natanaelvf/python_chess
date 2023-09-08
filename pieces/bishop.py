from typing import List
from pieces.piece import *

def get_bishop_moves(index : int, piece : int, board : List[int]) -> List[int]:
    available_moves = [index, piece]

    # Bishop move directions (diagonal)
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dx, dy in directions:
        x, y = index % 8 + dx, index // 8 + dy
        target_index = x + y * 8

        while 0 <= target_index < 64:
            target_piece = board[target_index]
            if target_piece == 0 or is_oponent_piece(piece, target_piece):
                available_moves.append(target_index)
                if target_piece != 0:
                    break

            # Move to the next square in the same diagonal direction
            x, y = x + dx, y + dy
            target_index = x + y * 8

    return available_moves