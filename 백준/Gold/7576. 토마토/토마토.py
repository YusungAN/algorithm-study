import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = []
for _ in range(m):
    graph.append(list(map(int, input().rstrip().split(' '))))
sx = 0
sy = 0
q = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            sx = j
            sy = i
            q.append((sx, sy, 0))
res = 0
while len(q) > 0:
    px, py, cnt = q.popleft()
    flag = False
    if px > 0 and graph[py][px-1] == 0:
        q.append((px-1, py, cnt+1))
        graph[py][px-1] = 1
        flag = True
    if px < n-1 and graph[py][px+1] == 0:
        q.append((px+1, py, cnt+1))
        graph[py][px+1] = 1
        flag = True
    if py > 0 and graph[py-1][px] == 0:
        q.append((px, py-1, cnt+1))
        graph[py-1][px] = 1
        flag = True
    if py < m-1 and graph[py+1][px] == 0:
        q.append((px, py+1, cnt+1))
        graph[py+1][px] = 1
        flag = True

    # if not flag:
    #     res = cnt
    #     break
    res = cnt

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit(0)

print(res)
