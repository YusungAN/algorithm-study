import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

graph = defaultdict(list)

n, m = map(int, input().split(' '))
ss = []
check = list(range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    ss.append(a)

visited = [False]*(n+1)
s = []
def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

    s.append(node)
    check.remove(node)
for i in ss:
    dfs(i)

for i in check:
    s.append(i)
print(*reversed(s))