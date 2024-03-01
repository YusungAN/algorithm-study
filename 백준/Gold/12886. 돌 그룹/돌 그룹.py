import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

if (A+B+C) % 3 != 0:
    print(0)
    exit(0)


def sort_abc(a, b, c):
    li = [a, b, c]
    li.sort()
    return li[0], li[1], li[2]

A, B, C = sort_abc(A, B, C)

q = deque()
q.append((A, B, C))
visited = [[False]*1501 for _ in range(1501)]
visited[A][B] = True
while q:
    a, b, c = q.popleft()
    if a == b == c:
        print(1)
        exit(0)
    
    na, nb, nc = sort_abc(a+a, b-a, c)
    # print(na, nb, nc)
    if b-a >= 0 and not visited[na][nb]:
        q.append((na, nb, nc))
        visited[na][nb] = True
    na, nb, nc = sort_abc(a, b+b, c-b)
    if c-b >= 0 and not visited[na][nb]:
        q.append((na, nb, nc))
        visited[na][nb] = True
    na, nb, nc = sort_abc(a+a, b, c-a)
    if c-a >= 0 and not visited[na][nb]:
        q.append((na, nb, nc))
        visited[na][nb] = True


print(0)