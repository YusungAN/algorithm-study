import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque([(n, 0, [n])])

visited = [False]*1000001
visited[n] = True
while q:
    now, cnt, li = q.popleft()
    if now == 1:
        print(cnt)
        print(*li)
        break
    if now % 3 == 0 and not visited[now//3]:
        tmp = li[:]
        tmp.append(now // 3)
        q.append((now//3, cnt+1, tmp))
        visited[now // 3] = True
    if now % 2 == 0 and not visited[now//2]:
        tmp = li[:]
        tmp.append(now // 2)
        q.append((now // 2, cnt + 1, tmp))
        visited[now // 2] = True
    if now - 1 > 0 and not visited[now-1]:
        tmp = li[:]
        tmp.append(now - 1)
        q.append((now -1, cnt + 1, tmp))
        visited[now -1] = True