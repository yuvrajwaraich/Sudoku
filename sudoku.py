import sudoku_gui


boards = [[[0, 0, 0, 2, 6, 0, 7, 0, 1],
           [6, 8, 0, 0, 7, 0, 0, 9, 0],
           [1, 9, 0, 0, 0, 4, 5, 0, 0],
           [8, 2, 0, 1, 0, 0, 0, 4, 0],
           [0, 0, 4, 6, 0, 2, 9, 0, 0],
           [0, 5, 0, 0, 0, 3, 0, 2, 8],
           [0, 0, 9, 3, 0, 0, 0, 7, 4],
           [0, 4, 0, 0, 5, 0, 0, 3, 6],
           [7, 0, 3, 0, 1, 8, 0, 0, 0]],

          [[0, 4, 0, 3, 1, 0, 0, 0, 0],
           [3, 0, 0, 0, 0, 6, 0, 5, 0],
           [0, 1, 0, 0, 7, 5, 8, 0, 0],
           [0, 2, 0, 5, 0, 0, 6, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [7, 0, 5, 0, 0, 3, 0, 1, 0],
           [0, 0, 6, 7, 4, 0, 0, 8, 0],
           [0, 7, 0, 6, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 5, 1, 0, 7, 0]],

          [[0, 0, 0, 0, 0, 0, 2, 0, 1],
           [0, 9, 0, 0, 5, 0, 8, 6, 0],
           [6, 0, 0, 0, 0, 0, 0, 9, 0],
           [0, 0, 0, 0, 0, 3, 0, 0, 0],
           [0, 0, 0, 9, 0, 0, 0, 0, 0],
           [7, 0, 0, 0, 6, 0, 9, 8, 0],
           [0, 0, 6, 0, 9, 0, 7, 5, 0],
           [8, 5, 0, 2, 0, 4, 0, 0, 0],
           [9, 7, 0, 0, 0, 0, 0, 0, 0]]]




def notInRow(b, x, num):
    for a in b[x]:
        if num == a:
            return False
    return True


def notInCol(b, y, num):
    for a in range(9):
        if num == b[a][y]:
            return False
    return True


def notInBox(b, x, y, num):
    row = x//3
    col = y//3

    for i in range(row*3, row*3 + 3):
        for j in range(col*3, col*3 + 3):
            if num == b[i][j]:
                return False
    return True


def isValid(b, x, y, num):
    return notInRow(b, x, num) and notInCol(b, y, num) and notInBox(b, x, y, num)


def solve(b):
    for row in range(9):
        for col in range(9):
            if b[row][col] == 0:
                for num in range(1, 10):
                    if isValid(b, row, col, num):
                        b[row][col] = num
                        sudoku_gui.good(b, row, col)
                        if solve(b) == 0:
                            sudoku_gui.bad(b, row, col)
                            b[row][col] = 0
                        else:
                            return 1
                if b[row][col] == 0:
                    return 0
    return 1