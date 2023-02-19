import sys

input = sys.stdin.readline

uf = [i for i in range(51)]

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

n, m = map(int, input().split(' '))
true_li = list(map(int, input().split(' ')))

check_li = []
for _ in range(m):
    p_li = list(map(int, input().split(' ')))
    if p_li[0] > 1:
        for i in p_li[2:]:
            union(p_li[1], i)
    check_li.append(p_li[1])

ans = 0
for i in check_li:
    if true_li[0] > 0:
        for j in true_li[1:]:
            if is_union(i, j):
                ans += 1
                break

print(m-ans)
