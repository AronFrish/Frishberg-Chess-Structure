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
        s = ""
        for row in self.board:
            s += (str(row) + "\n")
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