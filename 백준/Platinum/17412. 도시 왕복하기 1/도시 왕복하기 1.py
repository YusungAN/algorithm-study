import sys
from collections import deque

input = sys.stdin.readline

n, p = map(int, input().split())
graph = [[] for _ in range(n+1)]
cap = [[0]*(n+1) for _ in range(n+1)]
flow = [[0]*(n+1) for _ in range(n+1)]

for _ in range(p):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    cap[s][e] = 1


def max_flow():
    ans = 0

    while True:
        prev_visited = [0]*(n+1)
        q = deque()
        q.append(1)
        cap_min = float('inf')
        while q:
            now = q.popleft()
            for node in graph[now]:
                if prev_visited[node] == 0 and cap[now][node] > flow[now][node]:
                    prev_visited[node] = now
                    q.append(node)
                    # print(now, node)
                    cap_min = min(cap_min, cap[now][node]-flow[now][node])
                    if node == 2:
                        break

        if not prev_visited[2]:
            break

        s = 2
        while True:
            flow[s][prev_visited[s]] -= cap_min
            flow[prev_visited[s]][s] += cap_min
            s = prev_visited[s]
            if s == 1:
                break

        ans += cap_min
    return ans

print(max_flow())