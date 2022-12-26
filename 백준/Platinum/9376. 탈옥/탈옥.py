import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split(' '))
    sin = [['.']*(w+2)]
    p = []
    avail_exit = []
    for i in range(h):
        tmp = list('.'+input().rstrip()+'.')
        if '$' in tmp:
            for j in range(len(tmp)):
                if tmp[j] == '$':
                    p.append((j, i+1))
        sin.append(tmp)
    sin.append(['.']*(w+2))

    def bfs(sx, sy):
        dist = [[-1] * (w+2) for _ in range(h+2)]
        dist[sy][sx] = 0

        q = deque([])
        q.append((sx, sy))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < w+2 and 0 <= ny < h+2 and dist[ny][nx] == -1:
                    if sin[ny][nx] == '.' or sin[ny][nx] == '$':
                        dist[ny][nx] = dist[y][x]
                        q.appendleft((nx, ny))
                    elif sin[ny][nx] == '#':
                        dist[ny][nx] = dist[y][x]+1
                        q.append((nx, ny))
        return dist

    v1 = bfs(p[0][0], p[0][1])
    v2 = bfs(p[1][0], p[1][1])
    v3 = bfs(0, 0)

    _min = int(1e9)
    for i in range(h+2):
        for j in range(w+2):
            if v1[i][j] != -1 and v2[i][j] != -1 and v3[i][j] != -1:
                temp = v1[i][j] + v2[i][j] + v3[i][j]
                if sin[i][j] == '*':
                    continue
                if sin[i][j] == '#':
                    temp -= 2
                _min = min(_min, temp)

    print(_min)

