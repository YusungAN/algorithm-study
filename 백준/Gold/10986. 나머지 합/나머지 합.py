import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = list(map(int, input().split(' ')))
li = list(map(lambda x: x % m, li))

sums = [li[0]]+[0]*(n-1)
idxs = [0]*m

for i in range(n):
    if i == 0:
        idxs[li[0]] += 1
        continue
    sums[i] = (sums[i-1]+li[i]) % m
    idxs[sums[i]] += 1

#print(sums)
#print(idxs)
com = 0
for i in range(m):
    if i == 0:
        com += idxs[i]
    com += idxs[i]*(idxs[i]-1) // 2
print(com)