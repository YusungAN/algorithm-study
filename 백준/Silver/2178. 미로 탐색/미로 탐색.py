import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

q = deque()
q.append((0, 0, 1))
while len(q) > 0:
    px, py, cnt = q.popleft()
    graph[py][px] = 0
    if px == m-1 and py == n-1:
        print(cnt)
        break
    if px > 0 and graph[py][px-1] == 1:
        q.append((px-1, py, cnt+1))
        graph[py][px-1] = 0
    if px < m-1 and graph[py][px+1] == 1:
        q.append((px+1, py, cnt+1))
        graph[py][px+1] = 0
    if py > 0 and graph[py-1][px] == 1:
        q.append((px, py-1, cnt+1))
        graph[py-1][px] = 0
    if py < n-1 and graph[py+1][px] == 1:
        q.append((px, py+1, cnt+1))
        graph[py+1][px] = 0