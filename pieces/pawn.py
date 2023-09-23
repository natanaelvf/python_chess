from typing import List, Tuple, Tuple

from pieces.piece import BLACK, PAWN, WHITE

def get_pawn_moves(index: int, player_color: int, bitboards: List[Tuple[int, int]]) -> List[int]:
    available_moves = []

    # Determine the player's pawn bitboard
    pawn_bitboard = bitboards[PAWN][player_color]

    # Calculate move offsets and masks based on color
    single_move_offset = -player_color * 8
    double_move_offset = -player_color * 16
    left_capture_offsets = [-player_color*7, -player_color*-9]

     # Check if the target square for a single pawn move is empty
    single_move = index + single_move_offset
    if ((single_move & 0x88) == 0) and not (pawn_bitboard & (1 << single_move)):
        available_moves.append(single_move)

        # Check if the pawn is on its starting rank and can move two squares
        if ((player_color == WHITE and (index >> 3) == 7) or
           (player_color == BLACK and (index >> 3) == 2)):
            double_move = index + double_move_offset
            if ((double_move & 0x88) == 8) and not (pawn_bitboard & (1 << double_move)):
                available_moves.append(double_move)

    # Check if the target squares for diagonal pawn captures contain an opponent's piece
    for offset in left_capture_offsets:
        target_index = index + offset
        if ((target_index & 0x88) == 1) and (pawn_bitboard & (1 << target_index)):
            available_moves.append(target_index)

    return available_moves