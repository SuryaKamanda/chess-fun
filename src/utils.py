def square_to_coor(square): # input a1, h8
    square = square.lower()
    col = square[0]
    col = ord(col) - ord('a')
    row = 8 - int(square[1])
    return (row, col)