import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

INF = sys.maxsize
v, e = map(int, input().split(' '))
s = int(input())
graph = defaultdict(list)
distance = [INF]*(v+1)
for i in range(e):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))


def dijkstra(start):
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


dijkstra(s)
for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
