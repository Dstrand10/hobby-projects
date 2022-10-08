import numpy as np


class Board:

    def __init__(self, raw_board):
        self.board = self.createBoardDict(raw_board)
        self.nbrRows = len(raw_board.split("\n"))
        self.nbrCols = int(len(self.board) / len(raw_board.split("\n")))
        self.markedBoard = np.zeros((self.nbrRows, self.nbrCols))
        self.rowSum = np.zeros(self.nbrRows)
        self.colSum = np.zeros(self.nbrCols)
        self.scoreWhenWon = None
        self.bingoNbrIdx = None
        self.bingoNbr = None
        self.hasWon = False

    def createBoardDict(self, raw_board):
        board = {}
        for idx_row, row in enumerate(raw_board.split("\n")):
            values = [value for value in row.split(" ") if value != ""]
            for idx_col, value in enumerate(values):
                board[int(value)] = (idx_row, idx_col)
        return board

    def markNbr(self, bingoNbr, bingoNbrIdx):
        coord = self.board.get(bingoNbr, None)
        if coord is None:
            return
        else:
            self.markedBoard[coord[0]][coord[1]] = 1
            self.rowSum[coord[0]] += 1
            self.colSum[coord[1]] += 1
        if self.nbrRows in self.rowSum or self.nbrCols in self.colSum:
            self.bingoNbrIdx = bingoNbrIdx
            self.bingoNbr = bingoNbr
            self.setCalculateScore()
            self.hasWon = True

    def setCalculateScore(self):
        boardUnmarkedSum = 0
        for row_idx, row in enumerate(self.markedBoard):
            for col_idx, value in enumerate(row):
                if value == 0:
                    boardUnmarkedSum += list(self.board.keys())[list(self.board.values()).index((row_idx, col_idx))]
        self.scoreWhenWon = boardUnmarkedSum * self.bingoNbr


def main():
    with open('input.txt') as f:
        in_data = list(f.read().split("\n\n"))
        bingo_nbrs = list(map(int, in_data[0].split(",")))
        boards = []
        for raw_board in in_data[1:]:
            boards.append(Board(raw_board))

        for idxNbr, bingoNbr in enumerate(bingo_nbrs):
            for board in [board for board in boards if not board.hasWon]:
                board.markNbr(bingoNbr, idxNbr)

        sol1 = min(boards, key=lambda board: board.bingoNbrIdx).scoreWhenWon
        print(f"Solution 1: {sol1}")
        sol2 = max(boards, key=lambda board: board.bingoNbrIdx).scoreWhenWon
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
