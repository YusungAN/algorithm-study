import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
path = [list(input().rstrip()) for _ in range(N)]
s = input().rstrip()
s_len = len(s)

dx = []
dy = []
for i in range(1, K+1):
    dx.append(i)
    dy.append(0)
    dx.append(-i)
    dy.append(0)
    dx.append(0)
    dy.append(i)
    dx.append(0)
    dy.append(-i)


visited = [[[-1]*(s_len) for _ in range(M)] for _ in range(N)]

def dfs(x, y, s_idx):
    if s_idx == s_len-1:
        return 1
    
    if visited[y][x][s_idx] != -1:
        return visited[y][x][s_idx]
    
    visited[y][x][s_idx] = 0
    for i in range(4*K):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if path[ny][nx] == s[s_idx+1]:                
                visited[y][x][s_idx] += dfs(nx, ny, s_idx+1)

    return visited[y][x][s_idx]

ans = 0
for i in range(N):
    for j in range(M):
        if path[i][j] == s[0]:
            ans += dfs(j, i, 0)

print(ans)