import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, m = map(int, input().split(' '))
bing = [list(map(int, input().split(' '))) for _ in range(n)]

year = 0
while True:
    ice_cnt = 0
    start = (0, 0)
    flag = False
    for i in range(n):
        for j in range(m):
            if bing[i][j] != 0:
                start = (j, i)
                flag = True
                ice_cnt += 1

    if not flag:
        print(0)
        exit(0)

    visited = [[False]*m for _ in range(n)]
    check_cnt = 0
    w_cnt = [[0]*m for _ in range(n)]
    def dfs(x, y):
        global check_cnt
        visited[y][x] = True
        check_cnt += 1
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if bing[ny][nx] == 0:
                    w_cnt[y][x] += 1
                elif not visited[ny][nx]:
                    dfs(nx, ny)

    dfs(start[0], start[1])
    for y in range(n):
        for x in range(m):
            bing[y][x] = max(bing[y][x]-w_cnt[y][x], 0)

    year += 1
    if check_cnt != ice_cnt:
        break
print(year-1)
