import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

parents = [0]*(n+1)
visited = [False]*(n+1)
visited[1] = True
def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            parents[i] = start
            dfs(i)
            visited[i] = False

dfs(1)
for i in parents[2:]:
    print(i)
