import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, k = map(int, input().split(' '))

graph = [(0, float('inf'))]*100001

q = deque([])
q.append((n, 0))
graph[n] = (n, 0)

while q:
    now, cnt = q.popleft()
    if 2*now <= 100000 and graph[2*now][1] > cnt:
        q.append((2*now, cnt+1))
        graph[2 * now] = (now, cnt+1)
    if now+1 <= 100000 and graph[now+1][1] > cnt:
        q.append((now+1, cnt+1))
        graph[now+1] = (now, cnt+1)
    if now-1 >= 0 and graph[now-1][1] > cnt:
        q.append((now-1, cnt+1))
        graph[now - 1] = (now, cnt+1)

print(graph[k][1])
idx = k
res = [k]
while True:
    res.append(graph[idx][0])
    if graph[idx][0] == n:
        break
    idx = graph[idx][0]
if n == k:
    print(n)
    exit(0)
print(*reversed(res))