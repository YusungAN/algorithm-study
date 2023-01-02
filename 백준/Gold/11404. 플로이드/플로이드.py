import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    dist[a][b] = c if dist[a][b] > c else dist[a][b]

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[j][k] = min(dist[j][k], dist[j][i]+dist[i][k])

for y, i in enumerate(dist[1:]):
    for x, j in enumerate(i[1:]):
        if x == y:
            print(0, end=' ')
        else:
            if j == float('inf'):
                print(0, end=' ')
            else:
                print(j, end=' ')
    print('')

