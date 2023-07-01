from pieces import Pawn, Bishop, Rook, Knight, Queen, King
from board import *
import random

board = Board()

def random_piece(x, y):
    while True:
        rand = random.randint(0, 5)

        # Making sure there's no repeats
        if rand == 0 and board.count_pieces(0) >= 8:
            continue
        elif rand == 1 and board.count_pieces(1) >= 2:
            continue
        elif rand == 2 and board.count_pieces(2) >= 2:
            continue
        elif rand == 3 and board.count_pieces(3) >= 2:
            continue
        elif rand == 4 and board.count_pieces(4) >= 1:
            continue
        elif rand == 5 and board.count_pieces(5) >= 1:
            continue
        # Making sure there's no repeats

        if rand == 0:
            return Pawn(x, y, board)
        elif rand == 1:
            return Bishop(x, y, board)
        elif rand == 2:
            return Rook(x, y, board)
        elif rand == 3:
            return Knight(x, y, board)
        elif rand == 4:
            return Queen(x, y, board)
        elif rand == 5:
            return King(x, y, board)

def generate_random_board(n) :
    while (n!=0) :
        x = random.randint(0, 7)
        y = random.randint(0, 7)

        #preventing piece stacking
        if (board.get_piece(x, y) != " ") :
            continue
        #preventing piece stacking

        board.add_piece(random_piece(x, y))
        n -= 1

def run_simulation(n) :
    generate_random_board(n)
    for piece in board.all_pieces :
        if (not (piece.is_protected() and piece.is_protecting())) :
            return False, board, 0
    return True, board, board.num_protections()

f = open("output.txt", "r")
best_protections = int(f.readlines()[0].strip())
f.close()
best_board = None
while (True) :
    board = Board()
    result, board, protections = run_simulation(16)
    if (result and protections > best_protections) :
        best_protections = protections
        best_board = board
        f = open("output.txt", "w")
        f.write(str(protections) + "\n" + str(best_board))
        f.close()
        print("New best board found with " + str(best_protections) + " protections")