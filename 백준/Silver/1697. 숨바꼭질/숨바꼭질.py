import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [False]*100001

q = deque()
visited[n] = True
q.append((n, 0))

while q:
    now, second = q.popleft()
    if now == k:
        print(second)
        break
    if now*2 <= 100000 and not visited[now*2]:
        visited[now*2] = True
        q.append((now*2, second+1))
    if now+1 <= 100000 and not visited[now+1]:
        visited[now+1] = True
        q.append((now+1, second+1))
    if now - 1 >= 0 and not visited[now - 1]:
        visited[now - 1] = True
        q.append((now - 1, second + 1))
