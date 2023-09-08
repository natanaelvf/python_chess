from convertions.board_conversion import *

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
board = fen_to_board(fen)
fen = board_to_fen(board)
