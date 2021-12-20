import timeit


def load_input(file_name="in.txt"):
    res = []
    board = None
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                order = line.strip().split(",")
            else:
                if line == "\n":
                    if board:
                        res.append(board)
                    board = []
                else:
                    line = line.strip().split()
                    board.append([{"num": x, "state": False} for x in line])
    res.append(board)
    return res, order


def calculate_result(board, draw):
    unmarked_score = 0
    for row_of_winning_board in board:
        for num_of_winning_board in row_of_winning_board:
            if not num_of_winning_board["state"]:
                unmarked_score += int(num_of_winning_board["num"])
    return unmarked_score * int(draw)


def solve_pt1():
    boards, order = load_input()
    for draw in order:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, num in enumerate(row):
                    if num["num"] == draw:
                        num["state"] = True
                        skip = False
                        for c in range(len(row)):
                            if not board[j][c]["state"]:
                                skip = True
                                break
                        if not skip:
                            return calculate_result(board, draw)
                        skip = False
                        for c in range(len(row)):
                            if not board[c][k]["state"]:
                                skip = True
                                break
                        if not skip:
                            return calculate_result(board, draw)


def solve_pt2():
    boards, order = load_input()
    winning_boards = set()
    for draw in order:
        for i, board in enumerate(boards):
            if i in winning_boards:
                continue
            for j, row in enumerate(board):
                for k, num in enumerate(row):
                    if num["num"] == draw:
                        num["state"] = True
                        skip = False
                        for c in range(len(row)):
                            if not board[j][c]["state"]:
                                skip = True
                                break
                        if not skip:
                            winning_boards.add(i)
                            if len(winning_boards) == len(boards):
                                return calculate_result(board, draw)
                            break
                        skip = False
                        for c in range(len(row)):
                            if not board[c][k]["state"]:
                                skip = True
                                break
                        if not skip:
                            winning_boards.add(i)
                            if len(winning_boards) == len(boards):
                                return calculate_result(board, draw)
                            break


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1:{end - start} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Cas vykonavania pt2:{end - start} sec")
