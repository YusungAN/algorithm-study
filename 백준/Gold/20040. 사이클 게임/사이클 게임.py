import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

uf = [i for i in range(500001)]

def find(num):
    if uf[num] == num:
        return num
    uf[num] = find(uf[num])
    return uf[num]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return True
    uf[y] = x
    return False


n, m = map(int, input().split(' '))
end = 0
for i in range(1, m+1):
    a, b = map(int, input().split(' '))
    is_cycle = union(a, b)
    if is_cycle:
        if end == 0:
            end = i

print(end)
