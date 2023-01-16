import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[float('inf')]*n for _ in range(n)]
prev = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    if dist[a-1][b-1] > c:
        dist[a-1][b-1] = c
        prev[a-1][b-1] = a-1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[j][k] > dist[j][i]+dist[i][k]:
                dist[j][k] = dist[j][i]+dist[i][k]
                prev[j][k] = prev[i][k]

for y, i in enumerate(dist):
    for x, j in enumerate(i):
        if x == y:
            print(0, end=' ')
        else:
            if j == float('inf'):
                print(0, end=' ')
            else:
                print(j, end=' ')
    print('')

for i in range(n):
    for j in range(n):
        if i == j:
            print(0)
            continue
        if dist[i][j] == float('inf'):
            print(0)
            continue
        idx = j
        res = [j+1]
        while True:
            if prev[i][idx] == i:
                break
            res.append(prev[i][idx]+1)
            idx = prev[i][idx]
        res.append(i+1)
        print(len(res), end=' ')
        print(*reversed(res))
