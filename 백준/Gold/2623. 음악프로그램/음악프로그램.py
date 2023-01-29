import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))

graph = [[] for _ in range(n+1)]
indeg = [0]*(n+1)
q = deque()

for _ in range(m):
    li = list(map(int, input().split(' ')))
    for i in range(1, li[0]):
        graph[li[i]].append(li[i+1])
        indeg[li[i+1]] += 1

for i in range(1, n+1):
    if indeg[i] == 0:
        q.append(i)

res = []
while q:
    next = q.popleft()
    res.append(next)
    for i in graph[next]:
        if indeg[i] > 0:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)
if len(res) < n:
    print(0)
else:
    for i in res:
        print(i)
