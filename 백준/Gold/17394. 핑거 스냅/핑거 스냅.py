import sys
from collections import deque

input = sys.stdin.readline

primes = [True]*(10**6+1)
primes[0] = False
primes[1] = False
for i in range(2, 10**6+1):
    if primes[i]:
        for j in range(i*2, 10**6+1, i):
            primes[j] = False

#print('ok')
def bfs(n, a, b):
    q = deque([])
    visited = [False]*(10**6+1)
    q.append((n, 0))
    visited[n] = True
    while q:
        k, cnt = q.popleft()
        # print(k, cnt)
        if a <= k <= b and primes[k]:
            return cnt
        if not visited[k//2]:
            q.append((k//2, cnt+1))
            visited[k//2] = True
        if not visited[k//3]:
            q.append((k//3, cnt+1))
            visited[k//3] = True
        if k < 10**6 and not visited[k+1]:
            q.append((k + 1, cnt + 1))
            visited[k+1] = True
        if k > 0 and not visited[k-1]:
            q.append((k-1, cnt+1))
            visited[k-1] = True

    return -1


for i in range(int(input())):
    n, a, b = map(int, input().split(' '))
    print(bfs(n, a, b))