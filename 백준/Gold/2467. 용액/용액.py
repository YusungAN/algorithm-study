import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split(' ')))
li.sort()

p1 = 0
p2 = n-1
_min = int(1e10)
pidx1 = -1
pidx2 = -1
while p1 < p2:
    if _min > abs(li[p1]+li[p2]):
        _min = abs(li[p1]+li[p2])
        pidx1 = p1
        pidx2 = p2

    if li[p1]+li[p2] == 0:
        break

    if li[p1]+li[p2] > 0:
        p2 -= 1
    else:
        p1 += 1

print(li[pidx1], li[pidx2])