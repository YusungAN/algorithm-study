import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split(' '))
visited = [False]*(n+1)
dic = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split(' '))
    dic[a].append(b)
    dic[b].append(a)

res = []
def dfs(r):
    visited[r] = True
    res.append(r)
    dic[r].sort()
    isok = False
    for i in dic[r]:
        if not visited[i]:
            isok = True
            dfs(i)
    if not isok:
        return

dfs(r)
print(*res)




visited = [False]*(n+1)
q = deque([])

res = [r]
visited[r] = True
q.append(r)
cnt = 1
while len(q) > 0:
    u = q.popleft()
    dic[u].sort()
    for i in dic[u]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            cnt += 1
            res.append(i)

print(*res)