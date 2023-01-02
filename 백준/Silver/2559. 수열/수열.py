import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

li = list(map(int, input().split(' ')))

sums = []
_sum = 0
for i in li:
    _sum += i
    sums.append(_sum)

res = []

for i in range(n-k+1):
    if i == 0:
        res.append(sums[i+k-1])
        continue
    res.append(sums[i+k-1]-sums[i-1])

print(max(res))