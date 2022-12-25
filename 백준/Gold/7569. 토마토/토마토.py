import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split(' '))
graph = []
for _ in range(h):
    temp = []
    for _ in range(m):
        temp.append(list(map(int, input().rstrip().split(' '))))
    graph.append(temp)


sx = 0
sy = 0
sh = 0
q = deque()
for k in range(h):
    for i in range(m):
        for j in range(n):
            if graph[k][i][j] == 1:
                sx = j
                sy = i
                sh = k
                q.append((sx, sy, sh, 0))

res = 0
while len(q) > 0:
    px, py, ph, cnt = q.popleft()
    flag = False
    if px > 0 and graph[ph][py][px-1] == 0:
        q.append((px-1, py, ph, cnt+1))
        graph[ph][py][px-1] = 1
        flag = True
    if px < n-1 and graph[ph][py][px+1] == 0:
        q.append((px+1, py, ph, cnt+1))
        graph[ph][py][px+1] = 1
        flag = True
    if py > 0 and graph[ph][py-1][px] == 0:
        q.append((px, py-1, ph, cnt+1))
        graph[ph][py-1][px] = 1
        flag = True
    if py < m-1 and graph[ph][py+1][px] == 0:
        q.append((px, py+1, ph, cnt+1))
        graph[ph][py+1][px] = 1
        flag = True
    if ph > 0 and graph[ph-1][py][px] == 0:
        q.append((px, py, ph-1, cnt + 1))
        graph[ph-1][py][px] = 1
        flag = True
    if ph < h-1 and graph[ph+1][py][px] == 0:
        q.append((px, py, ph+1, cnt + 1))
        graph[ph+1][py][px] = 1
        flag = True

    res = cnt

for k in range(h):
    for i in range(m):
        for j in range(n):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)

print(res)