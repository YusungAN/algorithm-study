import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split(' '))
gem = [tuple(map(int, input().split(' '))) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort()
bag.sort()

ans = 0
q = []
idx = 0
for m in bag:
    while idx < n and gem[idx][0] <= m:
        heappush(q, -gem[idx][1])
        idx += 1
    if q:
        ans -= heappop(q)

print(ans)
