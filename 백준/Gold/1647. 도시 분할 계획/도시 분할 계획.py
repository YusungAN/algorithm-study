import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

edges = []
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    edges.append((c, a, b))

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

ans = 0
cost_li = []
for cost, s, e in edges:
    if not is_union(s, e):
        cost_li.append(cost)
        union(s, e)
        ans += cost

ans -= max(cost_li)

print(ans)
