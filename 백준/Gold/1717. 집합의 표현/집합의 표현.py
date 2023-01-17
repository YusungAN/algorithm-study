import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
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

for _ in range(m):
    o, a, b = map(int, input().split(' '))
    if o == 0:
        union(a, b)
    else:
        if is_union(a, b):
            print('YES')
        else:
            print('NO')
