import sys

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

start = 0
for i in range(v):
    li = list(map(int, input().split(' ')))
    for j in range(1, len(li), 2):
        if li[j] == -1:
            break
        graph[li[0]].append((li[j], li[j+1]))
    if start == 0 and len(graph[li[0]]) == 1:
        start = li[0]

visited = [False]*(v+1)
visited[start] = True
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


dfs(start, 0)
ans = 0
visited = [False]*(v+1)
visited[new_start] = True
dfs(new_start, 0)
print(ans)
