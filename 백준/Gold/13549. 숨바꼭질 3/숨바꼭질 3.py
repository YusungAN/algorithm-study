import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, k = map(int, input().split(' '))

graph = [float('inf')]*100001

q = deque([])
q.append((n, 0))
graph[n] = 0

while q:
    now, cnt = q.popleft()
    if 2*now <= 100000 and graph[2*now] > cnt:
        q.append((2*now, cnt))
        graph[2 * now] = cnt
    if now+1 <= 100000 and graph[now+1] > cnt:
        q.append((now+1, cnt+1))
        graph[now+1] = cnt+1
    if now-1 >= 0 and graph[now-1] > cnt:
        q.append((now-1, cnt+1))
        graph[now - 1] = cnt+1

print(graph[k])