import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    reverse_graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        reverse_graph[b].append(a)

    visited = [False]*(v+1)
    finish_order = []
    def dfs(node):
        visited[node] = True

        for i in graph[node]:
            if not visited[i]:
                dfs(i)
        finish_order.append(node)

    for i in range(1, v+1):
        if not visited[i]:
            dfs(i)

    visited = [False]*(v+1)
    cnt = 0
    for i in finish_order[::-1]:
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
