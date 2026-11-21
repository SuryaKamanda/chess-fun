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


