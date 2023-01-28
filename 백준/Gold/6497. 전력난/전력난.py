import sys

input = sys.stdin.readline

while True:
    m, n = map(int, input().split(' '))
    if m == 0 and n == 0:
        break
    edges = []
    ans = 0
    for _ in range(n):
        x, y, z = map(int, input().split(' '))
        edges.append((z, x, y))
        ans += z


    edges.sort()

    uf = [i for i in range(n+1)]

    def find(num):
        if uf[num] == num:
            return num
        uf[num] = find(uf[num])
        return uf[num]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return
        uf[y] = x

    def is_union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return True
        return False

    for cost, s, e in edges:
        if not is_union(s, e):
            union(s, e)
            ans -= cost

    print(ans)