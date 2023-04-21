import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    li = [[0]*(m*m) for _ in range(m*m)]
    for i in range(m*m):
        if (i // m == 0 or i // m == m-1) and (i % m == 0 or i % m == m-1):
            li[i][i] = 3
        elif (i // m == 0 or i // m == m-1) or (i % m == 0 or i % m == m-1):
            li[i][i] = 5
        else:
            li[i][i] = 8

    for i in range(m*m):
        for j in range(m*m):
            if i == j:
                continue
            ix = i % m
            iy = i // m
            jx = j % m
            jy = j // m

            if abs(ix-jx) <= 1 and abs(iy-jy) <= 1:
                li[i][j] = -1
    for i in range(1, m*m):
        for j in range(i+1, m*m):
            pivot = li[i][i]
            co = li[i][j]/pivot
            for k in range(i, m*m):
                li[j][k] -= li[i][k]*co
    ans = 1
    for i in range(1, m*m):
        ans *= li[i][i]
    print(round(ans))