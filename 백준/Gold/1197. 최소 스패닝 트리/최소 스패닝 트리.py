import sys
from heapq import heappop, heappush

input = sys.stdin.readline

v, e = map(int, input().split(' '))
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

q = [(0, 1)]
visited = [False]*(v+1)
ans = 0
while q:
    cost, now = heappop(q)
    if not visited[now]:
        ans += cost
        visited[now] = True
        for next, ncost in graph[now]:
            heappush(q, (ncost, next))

print(ans)
