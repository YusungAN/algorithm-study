import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split(' '))

li = []
start = (0, 0)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for y in range(h):
    tmp = list(input().rstrip())
    for i in range(w):
        if tmp[i] == 'C':
            start = (i, y)
    li.append(tmp)
sc = []
for i in range(4):
    nx = start[0] + dx[i]
    ny = start[1] + dy[i]
    if 0 <= nx < w and 0 <= ny < h and li[ny][nx] == '.':
        sc.append((nx, ny, i))

cnt_li = []
for sx, sy, pd in sc:
    visited = [[int(1e9)]*w for _ in range(h)]
    q = deque()
    q.append((sx, sy, 0, pd))
    # -1: 시작점 0: 상 1: 하 2: 좌 3: 우
    visited[sy][sx] = True
    visited[start[1]][start[0]] = True

    while q:
        x, y, cnt, prev_dir = q.popleft()
        if li[y][x] == 'C':
            cnt_li.append(cnt)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < w and 0 <= ny < h and li[ny][nx] != '*':
                ncnt = cnt
                if prev_dir != i:
                    ncnt += 1
                if visited[ny][nx] > ncnt:
                    q.append((nx, ny, ncnt, i))
                    visited[ny][nx] = ncnt

print(min(cnt_li))
