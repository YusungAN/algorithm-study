import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dij(graph, start, n):
    distance = [int(1e9)]*(n+1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            if d+i[1] < distance[i[0]]:
                distance[i[0]] = d+i[1]
                heappush(q, (d+i[1], i[0]))
    return distance


for _ in range(int(input())):
    n, m, t = map(int, input().split(' '))
    s, g, h = map(int, input().split(' '))
    graph = [[] for _ in range(n+1)]
    key_d = 0
    for i in range(m):
        a, b, d = map(int, input().split(' '))
        if (a == g and b == h) or (a == h and b == g):
            key_d = d
        graph[a].append((b, d))
        graph[b].append((a, d))
    des = [0]*t
    for i in range(t):
        des[i] = int(input())
    normal_d = dij(graph, s, n)
    res = []
    for i in des:
        # print(normal_d[i], normal_d[g], dij(graph, h, n)[i], key_d)
        # print(normal_d[i], normal_d[h], dij(graph, g, n)[i], key_d)
        if normal_d[i] == normal_d[g] + dij(graph, h, n)[i] + key_d or normal_d[i] == normal_d[h] + dij(graph, g, n)[i] + key_d:
            res.append(i)

    res.sort()
    print(*res)
