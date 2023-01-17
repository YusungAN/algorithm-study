import sys

input = sys.stdin.readline

n = int(input())
m = int(input())


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

for i in range(n):
    li = list(map(int, input().split(' ')))
    for j in range(n):
        if li[j] == 1:
            union(i+1, j+1)

li = list(map(int, input().split(' ')))
for i in range(len(li)-1):
    if not is_union(li[i], li[i+1]):
        print('NO')
        break
else:
    print('YES')
