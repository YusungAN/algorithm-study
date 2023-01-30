import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split(' '))
    maps = []
    start_p = []
    keys = set()
    ans = 0
    for y in range(h):
        tmp = list(input().rstrip())
        if y == 0 or y == h-1:
            for x in range(w):
                if tmp[x] != '*':
                    start_p.append((x, y))
                    if tmp[x] == '$':
                        ans += 1
                    elif tmp[x].islower():
                        keys.add(tmp[x])

        else:
            if tmp[0] != '*':
                start_p.append((0, y))
                if tmp[0] == '$':
                    ans += 1
                elif tmp[0].islower():
                    keys.add(tmp[0])
            if tmp[w-1] != '*':
                start_p.append((w-1, y))
                if tmp[w-1] == '$':
                    ans += 1
                elif tmp[w-1].islower():
                    keys.add(tmp[w-1])
        maps.append(tmp)
    s_keys = input().rstrip()

    if s_keys != '0':
        keys = keys.union(set(list(s_keys)))
    q = deque(start_p)
    visited = [[False]*w for _ in range(h)]
    for x, y in start_p:
        visited[y][x] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        # print(x, y)
        if ord('A') <= ord(maps[y][x]) <= ord('Z'):
            if maps[y][x].lower() in keys:
                pass
            else:
                for tx, ty in list(q):
                    if not (ord('A') <= ord(maps[ty][tx]) <= ord('Z')) or maps[ty][tx].lower() in keys:
                        q.append((x, y))
                        break
                else:
                    break
                continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                if maps[ny][nx] == '*':
                    continue
                if maps[ny][nx] == '$':
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    ans += 1
                elif ord('a') <= ord(maps[ny][nx]) <= ord('z'):
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    keys.add(maps[ny][nx])
                else:
                    q.append((nx, ny))
                    visited[ny][nx] = True
    print(ans)
