import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = []
for i in range(n):
    li.append(list(map(int, input().split(' '))))

q = deque()
visited = [[False]*m for _ in range(n)]
q.append([0, 0])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited[0][0] = True

flag = False


def bfs():
    global flag
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if 0 <= x < m and 0 <= y < n:
                if li[y][x] == 0 and not visited[y][x]:
                    q.append([x, y])
                    visited[y][x] = True
                elif li[y][x] > 0:
                    flag = True
                    li[y][x] += 1


cnt = 0
while True:
    visited = [[False] * m for _ in range(n)]
    flag = False
    q.append([0, 0])
    bfs()
    for i in range(n):
        for j in range(m):
            if li[i][j] > 2:
                li[i][j] = 0
            elif li[i][j] == 2:
                li[i][j] = 1
    if not flag:
        print(cnt)
        break
    cnt += 1
