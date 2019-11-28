from application import check

board = [[None, None, None], [None, None, None], [None, None, None]]
turn = "X"

class node:
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn

    def search(self):
        pass

def switch(turn):
    if turn == "X":
        return "O"
    else:
        return "X"