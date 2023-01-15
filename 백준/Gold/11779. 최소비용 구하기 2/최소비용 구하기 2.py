import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))

s, e = map(int, input().split(' '))

dist = [int(1e9)]*(n+1)
prevs = [0]*(n+1)


def dij(start, end):
    prevs[start] = start
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, now = heappop(q)
        if dist[now] < d:
            continue
        for next, cost in graph[now]:
            if d+cost < dist[next]:
                dist[next] = d+cost
                prevs[next] = now
                heappush(q, (d+cost, next))
    return dist[end]

print(dij(s, e))
idx = e
res = [e]
while True:
    if idx == s:
        break
    res.append(prevs[idx])
    idx = prevs[idx]
print(len(res))
print(*reversed(res))