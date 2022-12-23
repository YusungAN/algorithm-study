import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

e = []
for _ in range(m):
    e.append(tuple(map(int, input().split(' '))))

dist = [int(1e9)]*(n+1)


def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur, next, cost = e[j]
            if dist[cur] != int(1e9) and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False

is_nc = bf(1)

if is_nc:
    print(-1)
else:
    for i in dist[2:]:
        print(i if i != int(1e9) else -1)