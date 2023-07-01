def out_of_bounds(x, y) :
    return x < 0 or x > 7 or y < 0 or y > 7

def add_move(moves, x, y) :
    if not out_of_bounds(x, y) :
        moves.append((x, y))

class Pawn :
    def __init__(self, x, y, board) :
        self.x = x
        self.y = y
        self.board = board

    def __repr__(self) :
        return "P"
    
    def protection_moves(self) :
        moves = []
        add_move(moves, self.x - 1, self.y + 1)
        add_move(moves, self.x + 1, self.y + 1)
        return moves
    
    def is_protected(self) :
        for piece in self.board.all_pieces :
            protection_moves = piece.protection_moves()
            if (self.x, self.y) in protection_moves :
                return True
        return False
    
    def is_protecting(self) :
        for protected_move in self.protection_moves() :
            if (self.board.get_piece(protected_move[0], protected_move[1]) != ' ') :
                return True
        return False

class Bishop :
    def __init__(self, x, y, board) :
        self.x = x
        self.y = y
        self.board = board
    
    def __repr__(self) :
        return "B"

    def protection_moves(self) :
        moves = []

        #up right
        for i in range(1, 8) :
            cur_x = self.x + i
            cur_y = self.y + i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        #up left
        for i in range(1, 8) :
            cur_x = self.x - i
            cur_y = self.y + i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break

        #down right
        for i in range(1, 8) :
            cur_x = self.x + i
            cur_y = self.y - i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break

        #down left
        for i in range(1, 8) :
            cur_x = self.x - i
            cur_y = self.y - i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break 
        return moves
    
    def is_protected(self) :
        for piece in self.board.all_pieces :
            protection_moves = piece.protection_moves()
            if (self.x, self.y) in protection_moves :
                return True
        return False
    
    def is_protecting(self) :
        for protected_move in self.protection_moves() :
            if (self.board.get_piece(protected_move[0], protected_move[1]) != ' ') :
                return True
        return False
    
class Rook :
    def __init__(self, x, y, board) :
        self.x = x
        self.y = y
        self.board = board
    
    def __repr__(self) :
        return 'R'

    def protection_moves(self) :
        moves = []

        #up
        for i in range(1, 8) :
            cur_x = self.x
            cur_y = self.y + i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        #down
        for i in range(1, 8) :
            cur_x = self.x
            cur_y = self.y - i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break

        #right
        for i in range(1, 8) :
            cur_x = self.x + i
            cur_y = self.y
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break

        #left
        for i in range(1, 8) :
            cur_x = self.x - i
            cur_y = self.y
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break 
        return moves
    
    def is_protected(self) :
        for piece in self.board.all_pieces :
            protection_moves = piece.protection_moves()
            if (self.x, self.y) in protection_moves :
                return True
        return False
    
    def is_protecting(self) :
        for protected_move in self.protection_moves() :
            if (self.board.get_piece(protected_move[0], protected_move[1]) != ' ') :
                return True
        return False

class Knight :
    def __init__(self, x, y, board) :
        self.x = x
        self.y = y
        self.board = board
    
    def __repr__(self) :
        return 'N'

    def protection_moves(self) :
        moves = []
        add_move(moves, self.x + 1, self.y + 2)
        add_move(moves, self.x + 1, self.y - 2)
        add_move(moves, self.x - 1, self.y + 2)
        add_move(moves, self.x - 1, self.y - 2)
        add_move(moves, self.x + 2, self.y + 1)
        add_move(moves, self.x + 2, self.y - 1)
        add_move(moves, self.x - 2, self.y + 1)
        add_move(moves, self.x - 2, self.y - 1)
        return moves
    
    def is_protected(self) :
        for piece in self.board.all_pieces :
            protection_moves = piece.protection_moves()
            if (self.x, self.y) in protection_moves :
                return True
        return False
    
    def is_protecting(self) :
        for protected_move in self.protection_moves() :
            if (self.board.get_piece(protected_move[0], protected_move[1]) != ' ') :
                return True
        return False

class Queen :
    def __init__(self, x, y, board) :
        self.x = x
        self.y = y
        self.board = board
    
    def __repr__(self) :
        return 'Q'

    def protection_moves(self) :
        moves = []

        #up
        for i in range(1, 8) :
            cur_x = self.x
            cur_y = self.y + i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        #down
        for i in range(1, 8) :
            cur_x = self.x
            cur_y = self.y - i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break

        #right
        for i in range(1, 8) :
            cur_x = self.x + i
            cur_y = self.y
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break

        #left
        for i in range(1, 8) :
            cur_x = self.x - i
            cur_y = self.y
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break 

        #up right
        for i in range(1, 8) :
            cur_x = self.x + i
            cur_y = self.y + i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        #up left
        for i in range(1, 8) :
            cur_x = self.x - i
            cur_y = self.y + i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        #down right
        for i in range(1, 8) :
            cur_x = self.x + i
            cur_y = self.y - i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        #down left
        for i in range(1, 8) :
            cur_x = self.x - i
            cur_y = self.y - i
            add_move(moves, cur_x, cur_y)
            if (out_of_bounds(cur_x, cur_y)) :
                break
            elif (self.board.get_piece(cur_x, cur_y) != ' ') :
                break
        
        return moves
    
    def is_protected(self) :
        for piece in self.board.all_pieces :
            protection_moves = piece.protection_moves()
            if (self.x, self.y) in protection_moves :
                return True
        return False
    
    def is_protecting(self) :
        for protected_move in self.protection_moves() :
            if (self.board.get_piece(protected_move[0], protected_move[1]) != ' ') :
                return True
        return False

class King :
    def __init__(self, x, y, board) :
        self.x = x
        self.y = y
        self.board = board
    
    def __repr__(self) :
        return 'K'

    def protection_moves(self) :
        moves = []
        add_move(moves, self.x + 1, self.y + 1)
        add_move(moves, self.x + 1, self.y - 1)
        add_move(moves, self.x - 1, self.y + 1)
        add_move(moves, self.x - 1, self.y - 1)
        add_move(moves, self.x + 1, self.y)
        add_move(moves, self.x - 1, self.y)
        add_move(moves, self.x, self.y + 1)
        add_move(moves, self.x, self.y - 1)
        return moves
    
    def is_protected(self) :
        for piece in self.board.all_pieces :
            protection_moves = piece.protection_moves()
            if (self.x, self.y) in protection_moves :
                return True
        return False
    
    def is_protecting(self) :
        for protected_move in self.protection_moves() :
            if (self.board.get_piece(protected_move[0], protected_move[1]) != ' ') :
                return True
        return False