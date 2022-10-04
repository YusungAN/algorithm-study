import sys

input = sys.stdin.readline

li = []
cor = []
zeros = []


for i in range(9):
    li.append(list(map(int, input().rstrip().split(' '))))

for i in range(9):
    for j in range(9):
        if li[i][j] == 0:
            zeros.append((i, j))

def num_map(num):
    if 0 <= num <= 2:
        return 0
    elif 3 <= num <= 5:
        return 3
    else:
        return 6


def find_possible_num(x, y):
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in li[y]:
        if i != 0:
            res.remove(i)
    for i in range(9):
        if li[i][x] != 0 and li[i][x] in res:
            res.remove(li[i][x])

    x_start = num_map(x)
    y_start = num_map(y)

    for i in li[y_start][x_start:x_start+3]+li[y_start+1][x_start:x_start+3]+li[y_start+2][x_start:x_start+3]:
        if i != 0 and i in res:
            res.remove(i)

    return res


def sudoku(idx):
    if idx == len(zeros):
        for i in range(9):
            print(*li[i])
        exit(0)

    y = zeros[idx][0]
    x = zeros[idx][1]
    for i in find_possible_num(x, y):
        li[y][x] = i
        cor.append((x, y))
        sudoku(idx+1)
        li[y][x] = 0
        cor.remove((x, y))

sudoku(0)
