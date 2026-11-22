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

    def valid_pawn_move(self, start, end):
        start_row = start[0]
        start_col = start[1]
        end_row = end[0]
        end_col = end[1]
        piece = self.grid[start_row][start_col]
        target = self.grid[end_row][end_col]
        dr = end_row-start_row
        dc = abs(end_col-start_col)

        if piece == 'P':
            if dr == -1 and dc == 0:
                if target != '.':
                    return False
                else:
                    return True
            elif dr == -2 and dc == 0 and start_row == 6:
                front_check1 = self.grid[start_row-1][start_col]
                if front_check1 != '.':
                    return False
                elif target != '.':
                    return False
                else:
                    return True
            elif dr == -1 and dc == 1:
                if target == '.':
                    if self.en_passant != None:
                        if (end_row,end_col) == self.en_passant:
                            return True
                        else:
                            return False
                    else:                    
                        return False
                elif target.isupper():
                    return False
                else:
                    return True
            else:
                return False

        elif piece == 'p':
            if dr == 1 and dc == 0:
                if target != '.':
                    return False
                else:
                    return True
            elif dr == 2 and dc == 0 and start_row == 1:
                front_check2= self.grid[start_row+1][start_col]
                if front_check2 != '.':
                    return False
                elif target != '.':
                    return False
                else:
                    return True
            elif dr == 1 and dc == 1:
                if target == '.':
                    if self.en_passant != None:
                        if (end_row,end_col) == self.en_passant:
                            return True
                        else:
                            return False
                    else:                    
                        return False
                elif target.islower():
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    

    def is_valid_move(self, start, end):
        start_row = start[0]
        start_col = start[1]
        end_row = end[0]
        end_col = end[1]

        if not (0 <= end_col <= 7 and 0 <= end_row <= 7 and 0 <= start_col <= 7 and 0 <= start_row <= 7): # is still in the board?
            return False

        piece = self.grid[start_row][start_col]
        target = self.grid[end_row][end_col]
        dr = abs(end_row-start_row)
        dc = abs(end_col-start_col)
        cond = None

        if (start_row, start_col) == (end_row, end_col): # is piece not move?
            cond = False
        elif piece == '.': # is there a piece?
            cond = False
        elif self.turn == 'w' and piece.islower(): # is there really white?
            cond = False
        elif self.turn == 'b' and piece.isupper(): # is there really black?
            cond = False
        elif self.turn == 'w' and target.isupper(): # this is betraying?
            cond = False
        elif self.turn == 'b' and target.islower(): # this is betraying?
            cond = False
        elif piece.lower() == 'n' and (dr,dc) not in [(1,2), (2,1)]: # knight move
            cond = False
        elif piece.lower() == 'k' and (dr > 1 or dc > 1): # king move
            cond = False
        elif piece.lower() == 'p':
            cond = self.valid_pawn_move(start, end)
        else:
            cond = True

        return cond


    def make_move(self, start, end):
        cond = self.is_valid_move(start, end)
        
        if cond:
            start_row = start[0]
            start_col = start[1]
            end_row = end[0]
            end_col = end[1]
            piece = self.grid[start_row][start_col]
            dr = end_row-start_row
            self.grid[end_row][end_col] = self.grid[start_row][start_col]
            self.grid[start_row][start_col] = '.'

            if piece == 'P' and (end_row,end_col) == self.en_passant:
                self.grid[end_row + 1][end_col] = '.'
            elif piece == 'p' and (end_row,end_col) == self.en_passant:
                self.grid[end_row - 1][end_col] = '.'

            if piece.lower() == 'p' and abs(dr) == 2:
                self.en_passant = ((start_row + end_row)//2, end_col)
            else:
                self.en_passant = None

            if self.turn == 'w':
                self.turn = 'b'
            else:
                self.turn = 'w'
            return True
        else:
            return False

