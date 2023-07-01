class Board:

    # 0: pawn
    # 1: bishop
    # 2: rook
    # 3: knight
    # 4: queen
    # 5: king

    def __init__(self):
        self.board = []
        self.all_pieces = []
        for _ in range(8):
            self.board.append([" "]*8)

    def board_str(self):
        s = "  +---+---+---+---+---+---+---+---+\n"
        for y in range(7, -1, -1):
            s += str(y + 1) + " |"
            for x in range(8):
                piece = self.get_piece(x, y)
                s += " {} |".format(str(piece) if piece != " " else " ")
            s += "\n"
            s += "  +---+---+---+---+---+---+---+---+\n"
        s += "    a   b   c   d   e   f   g   h\n"
        return s

    def add_piece(self, piece):
        x = piece.x
        y = piece.y
        self.board[7-y][x] = piece
        self.all_pieces.append(piece)

    def get_all_pieces(self):
        return self.all_pieces
    
    def count_pieces(self, val) :
        count = 0
        desired_char = ""
        if val == 0 :
            desired_char = "P"
        elif val == 1 :
            desired_char = "B"
        elif val == 2 :
            desired_char = "R"
        elif val == 3 :
            desired_char = "N"
        elif val == 4 :
            desired_char = "Q"
        elif val == 5 :
            desired_char = "K"
        for piece in self.all_pieces :
            if str(piece) == desired_char :
                count += 1
        return count

    def get_piece(self, x, y):
        return self.board[7-y][x]

    def __str__(self):
        return self.board_str()
    
    def num_protections(self) :
        n = 0
        for piece in self.all_pieces :
            for protection in piece.protection_moves() :
                if (self.get_piece(protection[0], protection[1]) != " ") :
                    n += 1
        return n