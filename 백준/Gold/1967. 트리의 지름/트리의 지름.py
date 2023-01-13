import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for i in range(v-1):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [False]*(v+1)
visited[1] = True
ans = 0
new_start = 0
def dfs(s, dist):
    global ans
    global new_start
    flag = False
    for node, cost in graph[s]:
        if not visited[node]:
            flag = True
            visited[node] = True
            dfs(node, dist+cost)
            visited[node] = False

    if not flag:
        if ans < dist:
            ans = dist
            new_start = s


dfs(1, 0)
ans = 0
visited = [False]*(v+1)
visited[new_start] = True
dfs(new_start, 0)
print(ans)
