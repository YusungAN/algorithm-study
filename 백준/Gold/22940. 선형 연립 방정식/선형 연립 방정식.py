import sys

input = sys.stdin.readline

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split(' '))))

for col in range(n):
    if mat[col][col] == 0:
        for i in range(col+1, n):
            if mat[i][col]:
                for j in range(n+1):
                    mat[i][j], mat[col][j] = mat[col][j], mat[i][j]
                break
    for row in range(n):
        if row == col:
            continue
        if mat[row][col] == 0:
            continue

        cof = mat[row][col] / mat[col][col]
        for i in range(n+1):
            mat[row][i] -= cof*mat[col][i]


for i in range(n):
    print(round(mat[i][n]/mat[i][i]), end=' ')