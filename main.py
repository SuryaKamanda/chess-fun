from src.board import Board
from src.utils import square_to_coor

board = Board()
board.display()

while True:
    print(board.turn)
    start_player = input('Piece (example e2): ')
    if start_player.lower() == 'quit':
        break
    start_player = square_to_coor(start_player)
    end_player = input('To: ')
    if end_player.lower() == 'quit':
        break
    end_player = square_to_coor(end_player)
    board.make_move(start_player,end_player)

    board.display()
