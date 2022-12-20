import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = []
for _ in range(n):
    li.append(list(map(int, list(input().rstrip()))))

visited = [[[False]*m for _ in range(n)] for i in range(2)]
visited[0][0][0] = True

q = deque([])
q.append((0, 0, 1, False))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
while q:
    y, x, cnt, is_broken = q.popleft()
    # print(y, x, cnt, is_broken)
    if y == n-1 and x == m-1:
        print(cnt)
        exit(0)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx <= m-1 and 0 <= ny <= n-1:
            if li[ny][nx] == 0 and not visited[1 if is_broken else 0][ny][nx]:
                q.append((ny, nx, cnt+1, is_broken))
                if is_broken:
                    visited[1][ny][nx] = True
                else:
                    visited[0][ny][nx] = True
            elif li[ny][nx] == 1 and not is_broken:
                q.append((ny, nx, cnt+1, True))
                visited[1][ny][nx] = True

print(-1)
