from typing import List, Tuple, Tuple

from pieces.piece import BISHOP

def get_bishop_moves(index: int, piece_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    available_moves = []

    # Bishop move directions (diagonal)
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dx, dy in directions:
        x, y = index % 8 + dx, index // 8 + dy
        target_index = x + y * 8

        while 0 <= target_index < 64:
            target_piece = (bitboards[BISHOP][piece_color] | bitboards[1][piece_color]) & (1 << target_index)
            if target_piece == 0:
                available_moves.append(target_index)
            elif (bitboards[0][piece_color] | bitboards[1][piece_color]) & (1 << target_index):
                # It's an opponent's piece
                available_moves.append(target_index)
                break
            else:
                break
            x, y = x + dx, y + dy
            target_index = x + y * 8

    return available_moves