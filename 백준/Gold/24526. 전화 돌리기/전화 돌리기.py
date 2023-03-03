import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    reverse_graph[v].append(u)

visited = [False]*(n+1)
finished = [False]*(n+1)
cycle_node = []
def cycle(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            cycle(i)
        elif visited[i] and not finished[i]:
            cycle_node.append(i)
    finished[node] = True

for i in range(1, n+1):
    if not visited[i]:
        cycle(i)

visited = [False]*(n+1)
ans = n
def dfs(node):
    global ans
    visited[node] = True
    ans -= 1
    for i in reverse_graph[node]:
        if not visited[i]:
            dfs(i)

for i in cycle_node:
    if not visited[i]:
        dfs(i)

print(ans)