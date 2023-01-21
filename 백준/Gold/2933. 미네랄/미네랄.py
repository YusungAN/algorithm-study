import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r, c = map(int, input().split(' '))
cave = []
for _ in range(r):
    cave.append(list(input().rstrip()))
n = int(input())
op_li = list(map(int, input().split(' ')))

for i in range(len(op_li)):
    h = r-op_li[i]
    visited = [[False]*c for _ in range(r)]
    start = 0
    if i % 2 == 0:
        start = 0
        while start < c:
            if cave[h][start] == 'x':
                cave[h][start] = '.'
                break
            start += 1
    else:
        start = c-1
        while start >= 0:
            if cave[h][start] == 'x':
                cave[h][start] = '.'
                break
            start -= 1


    def dfs(x, y):
        visited[y][x] = True
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0 <= nx < c and 0 <= ny < r and cave[ny][nx] == 'x' and not visited[ny][nx]:
                dfs(nx, ny)

    for j in range(c):
        if cave[r-1][j] == 'x' and not visited[r-1][j]:
            dfs(j, r-1)

    min_gap = 10000
    for j in range(c):
        min_h = r
        gap = -1
        for h in range(r-1, -1, -1):
            if cave[h][j] == '.':
                continue
            if cave[h][j] == 'x':
                if visited[h][j]:
                    min_h = h
                else:
                    gap = min_h-h-1
                    if gap < min_gap:
                        min_gap = gap
                    break
    for j in range(c):
        for h in range(r-1, -1, -1):
            if cave[h][j] == '.':
                continue
            if cave[h][j] == 'x':
                if visited[h][j]:
                    min_h = h
                else:
                    cave[h][j] = '.'
                    cave[h+min_gap][j] = 'x'

for j in cave:
    print(''.join(j))
