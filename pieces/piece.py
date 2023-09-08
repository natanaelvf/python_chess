def is_white(piece : int) -> bool:
    # Determine the color based on the leftmost bit of the piece value
    return bool((piece >> 3) & 1)

def is_oponent_piece(piece : int, target_piece : int) -> bool:
    return (is_white(piece) and not is_white(target_piece)) or (not is_white(piece) and is_white(target_piece))