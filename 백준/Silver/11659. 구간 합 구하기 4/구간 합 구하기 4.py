import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
ij = []
li = list(map(int, input().split(' ')))
for i in range(m):
    ij.append(tuple(map(int, input().split(' '))))

sums = []
_sum = 0
for i in range(n):
    _sum += li[i]
    sums.append(_sum)
for i in range(m):
    print(sums[ij[i][1]-1]-(sums[ij[i][0]-2] if ij[i][0] != 1 else 0))
