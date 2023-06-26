import sys
from heapq import heappop, heappush

input = sys.stdin.readline

times = [tuple(map(int, input().split())) for _ in range(int(input()))]

times.sort(key=lambda x: x[0])
q = []
for s, f in times:
    heappush(q, f)
    if len(q) > 0:
        if q[0] <= s:
            heappop(q)

print(len(q))
