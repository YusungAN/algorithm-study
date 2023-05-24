import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(123)]
cap = [[0]*123 for _ in range(123)]
flow = [[0]*123 for _ in range(123)]

for _ in range(n):
    s, e, c = input().rstrip().split()
    ss = ord(s)
    ee = ord(e)
    graph[ss].append(ee)
    graph[ee].append(ss)
    cap[ss][ee] += int(c)
    cap[ee][ss] += int(c)


def max_flow():
    ans = 0

    while True:
        prev_visited = [0]*123
        q = deque()
        q.append(65)

        while q:
            now = q.popleft()
            for node in graph[now]:
                if prev_visited[node] == 0 and cap[now][node] > flow[now][node]:
                    prev_visited[node] = now
                    q.append(node)
                    if node == 90:
                        break

        if not prev_visited[90]:
            break

        cap_min = float('inf')
        s = 90
        while True:
            cap_min = min(cap_min, cap[prev_visited[s]][s]-flow[prev_visited[s]][s])
            s = prev_visited[s]
            if s == 65:
                break
        s = 90
        while True:
            flow[s][prev_visited[s]] -= cap_min
            flow[prev_visited[s]][s] += cap_min
            s = prev_visited[s]
            if s == 65:
                break

        ans += cap_min
    return ans

print(max_flow())