import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+m+3)]
cap = [[0]*(n+m+3) for _ in range(n+m+3)]
flow = [[0]*(n+m+3) for _ in range(n+m+3)]

src = 0
sink = n+m+1
other = n+m+2
# 사람: 1~N ,일: N+1~N+M
graph[src].append(other)
graph[other].append(src)
cap[src][other] = k
for i in range(1, n+1):
    li = list(map(int, input().split()))
    graph[src].append(i)
    graph[i].append(src)
    cap[src][i] = 1
    graph[other].append(i)
    graph[i].append(other)
    cap[other][i] = 1
    for j in li[1:]:
        graph[i].append(n+j)
        graph[n+j].append(i)
        cap[i][n+j] = 1

for j in range(n+1, n+m+1):
    graph[j].append(sink)
    graph[sink].append(j)
    cap[j][sink] = 1


def max_flow():
    ans = 0

    while True:
        prev_visited = [-1]*(n+m+3)
        q = deque()
        q.append(src)
        while q:
            now = q.popleft()
            for node in graph[now]:
                if prev_visited[node] == -1 and cap[now][node] > flow[now][node]:
                    prev_visited[node] = now
                    q.append(node)
                    if node == sink:
                        break

        if prev_visited[sink] == -1:
            break
        cap_min = float('inf')
        s = sink
        while True:
            cap_min = min(cap_min, cap[prev_visited[s]][s]-flow[prev_visited[s]][s])
            s = prev_visited[s]
            if s == src:
                break
        s = sink
        while True:
            flow[s][prev_visited[s]] -= cap_min
            flow[prev_visited[s]][s] += cap_min
            s = prev_visited[s]
            if s == src:
                break
        ans += cap_min
    return ans

print(max_flow())