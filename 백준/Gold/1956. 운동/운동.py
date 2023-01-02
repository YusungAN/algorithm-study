import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

dist = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    dist[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[j][k] = min(dist[j][k], dist[j][i]+dist[i][k])

_min = float('inf')
for i in range(1, n+1):
    if _min > dist[i][i]:
        _min = dist[i][i]

if _min == float('inf'):
    print(-1)
else:
    print(_min)