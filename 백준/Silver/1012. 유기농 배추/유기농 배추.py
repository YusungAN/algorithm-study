import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

t = int(input())
li = []
for _ in range(t):
    m, n, k = map(int, input().split(' '))
    li = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a, b = map(int, input().split(' '))
        li[b][a] = 1


    def dfs(x, y):
        li[y][x] = 0
        # print('asdf')
        isok = False
        if y > 0 and li[y - 1][x] == 1:
            isok = True
            dfs(x, y - 1)
        if x > 0 and li[y][x - 1] == 1:
            isok = True
            dfs(x - 1, y)
        if y < n - 1 and li[y + 1][x] == 1:
            isok = True
            dfs(x, y + 1)
        if x < m - 1 and li[y][x + 1] == 1:
            isok = True
            dfs(x + 1, y)
        if not isok:
            return

    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                dfs(j, i)
                cnt += 1
    print(cnt)


