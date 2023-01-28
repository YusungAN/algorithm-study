import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split(' '))
god_li = [tuple(map(int, input().split(' '))) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        graph[i].append([j, ((god_li[i][0]-god_li[j][0])**2 + (god_li[i][1]-god_li[j][1])**2)**(1/2)])
        graph[j].append([i, ((god_li[i][0] - god_li[j][0]) ** 2 + (god_li[i][1] - god_li[j][1]) ** 2) ** (1 / 2)])

for i in range(m):
    s, e = map(int, input().split(' '))
    s -= 1
    e -= 1
    for idx, node in enumerate(graph[s]):
        if node[0] == e:
            graph[s][idx][1] = 0
            break
    for idx, node in enumerate(graph[e]):
        if node[0] == s:
            graph[e][idx][1] = 0
            break

ans = 0
q = [(0, 0)]
visited = [False]*(n+1)

while q:
    cost, now = heappop(q)
    if not visited[now]:
        ans += cost
        visited[now] = True
        for next, ncost in graph[now]:
            heappush(q, (ncost, next))

print('{:.2f}'.format(round(ans, 2)))
