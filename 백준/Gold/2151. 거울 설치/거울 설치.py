import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
room = [list(input().rstrip()) for _ in range(n)]

start = (-1, -1)
end = (-1, -1)
visited = [[[-1]*4 for _ in range(n)] for _ in range(n)]


def dir_idx(dirX, dirY):
    if dirX == 1 and dirY == 0:
        return 0
    
    if dirX == -1 and dirY == 0:
        return 1
    
    if dirX == 0 and dirY == 1:
        return 2
    
    if dirX == 0 and dirY == -1:
        return 3


q = deque()

for i in range(n):
    for j in range(n):
        if room[i][j] == '#':
            if start[0] == -1:
                start = (i, j)
                if i+1 < n and room[i+1][j] != '*':
                    q.append((i, j, 0, 1))
                    visited[i][j][2] = 0
                if i-1 >= 0 and room[i-1][j] != '*':
                    q.append((i, j, 0, -1))
                    visited[i][j][3] = 0
                if j+1 < n and room[i][j+1] != '*':
                    q.append((i, j, 1, 0))
                    visited[i][j][0] = 0
                if j-1 >= 0 and room[i][j-1] != '*':
                    q.append((i, j, -1, 0))
                    visited[i][j][1] = 0
            else:
                end = (i, j)

ans = 251
while q:
    y, x, dirX, dirY = q.popleft()
    # print(x, y, dirX, dirY, visited[y][x][dir_idx(dirX, dirY)])
    if y == end[0] and x == end[1]:
        ans = min(ans, visited[y][x][dir_idx(dirX, dirY)])
    

    ny = y+dirY
    nx = x+dirX
    if 0 <= ny < n and 0 <= nx < n and not room[ny][nx] == '*':
        if visited[ny][nx][dir_idx(dirX, dirY)] == -1 or visited[ny][nx][dir_idx(dirX, dirY)] > visited[y][x][dir_idx(dirX, dirY)]:
            visited[ny][nx][dir_idx(dirX, dirY)] = visited[y][x][dir_idx(dirX, dirY)]
            q.append((ny, nx, dirX, dirY))

    

    if room[y][x] == '!':
        if dirY != 0:
            ny = y
            for dx in [-1, 1]:
                nx = x+dx
                if ny < 0 or ny >= n or nx >= n or nx < 0:
                    continue
                if room[ny][nx] == '*':
                    continue
                if visited[ny][nx][dir_idx(dx, 0)] == -1 or visited[ny][nx][dir_idx(dx, 0)] > visited[y][x][dir_idx(dirX, dirY)]:
                    visited[ny][nx][dir_idx(dx, 0)] = visited[y][x][dir_idx(dirX, dirY)]+1
                    q.append((ny, nx, dx, 0))
        else:
            nx = x
            for dy in [-1, 1]:
                ny = y+dy
                if ny < 0 or ny >= n or nx >= n or nx < 0:
                    continue

                if room[ny][nx] == '*':
                    continue
                if visited[ny][nx][dir_idx(0, dy)] == -1 or visited[ny][nx][dir_idx(0, dy)] > visited[y][x][dir_idx(dirX, dirY)]:
                    visited[ny][nx][dir_idx(0, dy)] = visited[y][x][dir_idx(dirX, dirY)]+1
                    q.append((ny, nx, 0, dy))

print(ans)