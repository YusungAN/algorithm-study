import sys

input = sys.stdin.readline
n = int(input())

li = list(map(int, input().split(' ')))
res = []
p1, p2 = 0, 1
while True:
    if p1 == n-1:
        break
    elif p2 == n - 1 and li[p1] == li[p2]:
        res += [-1]*(p2-p1)
        break
    elif li[p1] == li[p2]:
        p2 += 1
    elif li[p1] != li[p2]:
        res += [p2+1]*(p2-p1)
        p1 = p2
        p2 += 1

for i in res:
    print(i, end=' ')

print('-1')