import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split(' '))

li = []
for _ in range(n):
    li.append(list(input().rstrip()))


q = deque()

q.append((0, 0))
visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
            if li[ny][nx] == '0':
                visited[ny][nx] = visited[y][x]
                q.appendleft((nx, ny))
            else:
                visited[ny][nx] = visited[y][x]+1
                q.append((nx, ny))

print(visited[n-1][m-1])