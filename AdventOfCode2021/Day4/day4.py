def mark_boards(bingo_nbr, boards):
    for board in boards:
        for idx_row, row in enumerate(board):
            for idx_value, value in enumerate(row):
                if value[0] == bingo_nbr:
                    board[idx_row][idx_value] = (value[0], 1)


def check_if_bingo(board):
    for row in board:
        row_bingo = 0
        for value in row:
            row_bingo += value[1]
        if row_bingo == 5:
            return board

    for idx_row in range(len(board)):
        column_bingo = 0
        for idx_value in range(len(board[0])):
            column_bingo += board[idx_value][idx_row][1]
        if column_bingo == 5:
            return board
    return None


def calculateScore(bingo_board, bingo_nbr):
    unmarked_value_sum = 0
    for row in bingo_board:
        for value in row:
            if value[1] == 0:
                unmarked_value_sum += value[0]
    return unmarked_value_sum * bingo_nbr


def func1(bingo_nbrs, boards):
    for idx_bingo_nbr, bingo_nbr in enumerate(bingo_nbrs):
        mark_boards(bingo_nbr, boards)

        for board in boards:
            bingo_board = check_if_bingo(board)
            if bingo_board is not None:
                print(bingo_board)
                print("index bingo nbr " + str(idx_bingo_nbr))
                print("bingo_nbr: " + str(bingo_nbr))
                score = calculateScore(bingo_board, bingo_nbr)
                print("score: " + str(score))
                return score


def func2(bingo_nbrs, boards):
    bingo_board_order = []

    for idx_bingo_nbr, bingo_nbr in enumerate(bingo_nbrs):
        mark_boards(bingo_nbr, boards)
        for idx_board, board in enumerate(boards):

            if check_if_bingo(board) is not None and idx_board not in [x[0] for x in bingo_board_order]:
                bingo_board_order.append((idx_board, idx_bingo_nbr, board.copy()))
                boards.remove(board)

    print(bingo_board_order)

    latest_bingo_turn = 0
    latest_board = None
    for _, idx, bingo_board in bingo_board_order:
            if idx > latest_bingo_turn:
                latest_bingo_turn = idx
                latest_board = bingo_board
    print(latest_bingo_turn)
    for row in latest_board:
        print(row)
    print(calculateScore(latest_board, bingo_nbrs[latest_bingo_turn]))



    #return calculateScore(boards[bingo_board_order[idx_to_save][0]], bingo_nbrs[bingo_board_order[idx_to_save][1]])




def main():
    with open('input.txt') as f:
        in_data = list(f.read().split("\n\n"))
        bingo_nbrs = list(map(int, in_data[0].split(",")))
        boards = []
        for raw_board in in_data[1:]:
            tmp_board = []
            for board_row in raw_board.split("\n"):
                tmp_row_with_correct_tuple_calues = []
                tmp_row = board_row.split(" ")
                for value in tmp_row:
                    if value == "":
                        continue
                    else:
                        tmp_row_with_correct_tuple_calues.append((int(value), 0))
                tmp_board.append(tmp_row_with_correct_tuple_calues)
            boards.append(tmp_board)

        #sol1 = func1(bingo_nbrs.copy(), boards.copy())
        #print(f"Solution 1: {sol1}")

        sol2 = func2(bingo_nbrs.copy(), boards.copy())
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()