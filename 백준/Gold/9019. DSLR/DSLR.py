import sys
from collections import deque

input = sys.stdin.readline

def d(n):
    return (2*n) % 10000

def s(n):
    return n-1 if n > 0 else 9999

def l(n):
    d = [(n//1000)%10, (n//100)%10, (n//10)%10, n%10]
    return d[0] + d[3]*10 + d[2]*100 + d[1]*1000

def r(n):
    d = [(n//1000)%10, (n//100)%10, (n//10)%10, n%10]
    return d[2] + d[1]*10 + d[0]*100 + d[3]*1000


for _ in range(int(input())):
    st, e = map(int, input().split(' '))
    q = deque()
    q.append(('', st))
    visited = [False]*10000
    while q:
        ops, now = q.popleft()
        if now == e:
            print(ops)
            break
        next = d(now)
        if not visited[next]:
            q.append((ops+'D', next))
            visited[next] = True
        next = s(now)
        if not visited[next]:
            q.append((ops + 'S', next))
            visited[next] = True
        next = l(now)
        if not visited[next]:
            q.append((ops + 'L', next))
            visited[next] = True
        next = r(now)
        if not visited[next]:
            q.append((ops + 'R', next))
            visited[next] = True