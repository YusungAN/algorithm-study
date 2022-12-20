import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

INF = float('inf')
v, e = map(int, input().split(' '))
graph = defaultdict(list)
for i in range(e):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split(' '))

def dijkstra(start, end):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            if d+i[1] < distance[i[0]]:
                distance[i[0]] = d+i[1]
                heapq.heappush(q, (d+i[1], i[0]))
    return distance[end]

res = min(dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, v), dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, v))
print(res if res != INF else -1)