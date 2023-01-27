import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
star_li = [tuple(map(float, input().split(' '))) for _ in range(n)]
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(i+1, n):
        graph[i].append((j, ((star_li[i][0]-star_li[j][0])**2 + (star_li[i][1]-star_li[j][1])**2)**(1/2)))
        graph[j].append((i, ((star_li[i][0] - star_li[j][0]) ** 2 + (star_li[i][1] - star_li[j][1]) ** 2) ** (1 / 2)))


q = [(0, 1)]
visited = [False]*(n+1)
ans = 0
while q:
    cost, now = heappop(q)
    if not visited[now]:
        ans += cost
        visited[now] = True
        for next, ncost in graph[now]:
            heappush(q, (ncost, next))

print(ans)
