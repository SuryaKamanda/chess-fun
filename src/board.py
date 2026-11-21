class Board:
    def __init__(self):
        self.grid = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.turn = 'w'
        self.castling = {
            'k': True,
            'q': True,
            'K': True,
            'Q': True
        }
        self.en_passant = None

    def display(self):
        for i, r in enumerate(self.grid):
            print(8-i, " ".join(r))
        print('  a b c d e f g h')

    def make_move(self, start, end):
        start_row = start[0]
        start_col = start[1]
        end_row = end[0]
        end_col = end[1]
        piece = self.grid[start_row][start_col]

        if piece == '.':
            cond = False
        elif self.turn == 'w':
            if piece.islower() :
                cond = False
            else:
                cond = True
        elif self.turn == 'b':
            if piece.isupper() :
                cond = False
            else:
                cond = True
        else:
            cond = False
        
        if cond:
            self.grid[end_row][end_col] = self.grid[start_row][start_col]
            self.grid[start_row][start_col] = '.'
            if self.turn == 'w':
                self.turn = 'b'
            else:
                self.turn = 'w'
            return True
        else:
            return False

