import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split(' '))
li = list(map(int, input().split(' ')))


cnt = 0
for size in range(1, n+1):
    if size % 2 == 1:
        for i in combinations(li, size):
            tmp = 1
            for j in i:
                tmp *= j
            cnt += m // tmp
    else:
        for i in combinations(li, size):
            tmp = 1
            for j in i:
                tmp *= j
            cnt -= m // tmp

print(cnt)