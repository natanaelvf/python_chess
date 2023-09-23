from typing import List, Tuple


def get_knight_moves(index: int, piece_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    available_moves = []

    # Knight move offsets
    knight_offsets = [-17, -15, -10, -6, 6, 10, 15, 17]

    for offset in knight_offsets:
        target_index = index + offset
        if 0 <= target_index < 64:
            target_piece = (bitboards[0][piece_color] | bitboards[1][piece_color]) & (1 << target_index)
            if target_piece == 0:
                available_moves.append(target_index)
            elif (bitboards[0][piece_color] | bitboards[1][piece_color]) & (1 << target_index):
                # It's an opponent's piece
                available_moves.append(target_index)

    return available_moves