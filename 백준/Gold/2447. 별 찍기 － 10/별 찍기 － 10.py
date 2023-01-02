import sys

N = int(sys.stdin.readline().rstrip())

li = [[0 for j in range(N)] for i in range(N)]


def square(n):
    if n == 3:
        li[0][:3] = [1, 1, 1]
        li[1][:3] = [1, 0, 1]
        li[2][:3] = [1, 1, 1]
    else:
        square(n//3)
        for i in range(3):
            for j in range(3):
                if i == 0 and j == 0:
                    continue
                if i == 1 and j == 1:
                    continue
                for k in range(n//3):
                    li[(n//3)*i+k][(n//3)*j:(n//3)*(j+1)] = li[k][:(n//3)]


square(N)

for i in range(N):
    for j in range(N):
        if li[i][j] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
