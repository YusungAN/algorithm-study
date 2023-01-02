import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split(' '))
visited = [False]*(n+1)
dic = defaultdict(list)
q = deque([])
for i in range(m):
    a, b = map(int, input().split(' '))
    dic[a].append(b)
    dic[b].append(a)
res = [0]*(n+1)
visited[r] = True
q.append(r)
cnt = 1
res[r] = cnt
while len(q) > 0:
    u = q.popleft()
    dic[u].sort(reverse=True)
    for i in dic[u]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            cnt += 1
            res[i] = cnt

for i in res[1:]:
    print(i)