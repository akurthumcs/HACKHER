import tile

class grid:
    row, cols = None
    board = None

    def __init__(self, cols, rows):
        self.cols =cols
        self.row = rows
        self.board = [[tile] * cols] * rows

    def __initGridBoard__(self):
        for ver in self(self.cols):
            for hor in self(self.row):
                self[hor, ver].setWalkable(True)

    def getTile(self, hor, ver):
        return self.board[hor][ver]
    
    def setTile(self, hor, ver, tile):
        self.board[hor][ver] = tile

    
    