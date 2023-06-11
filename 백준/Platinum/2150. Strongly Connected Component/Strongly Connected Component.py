import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
reverse_graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
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
temp_li = []
temp = []


def dfs2(node, depth):
    global temp
    global cnt
    visited[node] = True
    temp.append(node)
    for i in reverse_graph[node]:
        if not visited[i]:
            dfs2(i, depth+1)

    if depth == 0:
        temp.sort()
        temp_li.append(temp)
        temp = []
        cnt += 1

for i in finish_order[::-1]:
    if not visited[i]:
        dfs2(i, 0)

print(cnt)
temp_li.sort(key=lambda x: x[0])
for i in temp_li:
    i.append(-1)
    print(*i)
