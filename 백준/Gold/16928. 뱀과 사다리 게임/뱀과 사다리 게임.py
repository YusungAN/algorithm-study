import sys
from collections import deque

input = sys.stdin.readline

game = [0]*101
for i in range(1, 101):
    game[i] = i
n, m = map(int, input().split(' '))
for _ in range(n+m):
    a, b = map(int, input().split(' '))
    game[a] = b

q = deque([])
q.append((1, 0))
visited = [False]*101
visited[1] = True

while q:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        break

    for i in range(1, 7):
        if now+i <= 100 and not visited[now+i]:
            q.append((game[now+i], cnt+1))
            visited[now+i] = True

