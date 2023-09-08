from typing import List

def get_pawn_moves(index: int, piece: int, board: List[int]) -> List[int]:
    available_moves = [index, piece]

    is_white = (piece >> 3) & 1

    # Lookup table for move offsets and masks based on color
    offsets = [-8, -16] if is_white else [8, 16]

    left_capture_offset = -7 if is_white else 7
    right_capture_offset = -9 if is_white else 9

    # Check if the target square for a single pawn move is empty
    single_move = index + offsets[0]
    if 0 <= single_move < 64 and (board[single_move] == 0):
        available_moves.append(single_move)

        # Check if the pawn is on its starting rank and can move two squares
        double_move = index + offsets[1]
        if ((is_white and 48 <= index <= 55) or (not is_white and 8 <= index <= 15)) and (board[double_move] == 0):
            available_moves.append(double_move)

    # Check if the target squares for diagonal pawn captures contain an opponent's piece
    left_capture = index + left_capture_offset
    if 0 <= left_capture < 64 and ((piece >> 3) != (board[left_capture] >> 3)) and board[left_capture] != 0:
        available_moves.append(left_capture)

    right_capture = index + right_capture_offset
    if 0 <= right_capture < 64 and ((piece >> 3) != (board[right_capture] >> 3)) and board[right_capture] != 0:
        available_moves.append(right_capture)

    return available_moves