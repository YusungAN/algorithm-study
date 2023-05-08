import sys

input = sys.stdin.readline

edges = []
N = int(input())
pl = [list(map(int, input().split(' ')))+[i+1] for i in range(N)]
pl.sort()
for i in range(N-1):
    edges.append((abs(pl[i][0]-pl[i+1][0]), pl[i][3], pl[i+1][3]))
pl.sort(key=lambda x:x[1])
for i in range(N-1):
    edges.append((abs(pl[i][1]-pl[i+1][1]), pl[i][3], pl[i+1][3]))
pl.sort(key=lambda x:x[2])
for i in range(N-1):
    edges.append((abs(pl[i][2]-pl[i+1][2]), pl[i][3], pl[i+1][3]))

uf = [i for i in range(N+1)]


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
edges.sort()
for cost, s, e in edges:
    if not is_union(s, e):
        union(s, e)
        ans += cost

print(ans)