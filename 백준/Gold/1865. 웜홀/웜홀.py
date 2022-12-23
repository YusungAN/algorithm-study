import sys

input = sys.stdin.readline

for _ in range(int(input())):

    n, m, w = map(int, input().split(' '))

    e = []
    for _ in range(m):
        a, b, c = map(int, input().split(' '))
        e.append((a, b, c))
        e.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split(' '))
        e.append((a, b, -c))

    #print(e)
    dist = [0]*(n+1)


    def bf(start):
        dist[start] = 0
        for i in range(n):
            for j in range(2*m+w):
                cur, next, cost = e[j]
                # print(dist, e[j])
                if dist[cur] != int(1e9) and dist[next] > dist[cur] + cost:
                    dist[next] = dist[cur] + cost
                    if i == n - 1:
                        return True
        return False

    is_nc = bf(1)
    #print(dist, is_nc)
    if is_nc:
        print('YES')
    else:
        print('NO')