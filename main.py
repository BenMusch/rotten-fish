from chess import uci, Move, Board

board = Board()
engine = uci.popen_engine("/Users/ben/src/Stockfish/src/stockfish")

while True:
    move = input("move: ")
    if move.startswith("fen "):
        board.set_fen(move[4:])
        continue
    board.push(Move.from_uci(move))
    engine.position(board)
    print(engine.go(depth=15))
