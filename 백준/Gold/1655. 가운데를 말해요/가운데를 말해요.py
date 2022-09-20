import sys
import heapq

input = sys.stdin.readline

n = int(input())

lh = []
rh = []

for i in range(n):
    a = int(input())
    if len(lh) == len(rh):
        heapq.heappush(lh, -a)
    else:
        heapq.heappush(rh, a)

    if len(rh) > 0 and -1*lh[0] > rh[0]:
        p = -1*heapq.heappop(lh)
        q = -1*heapq.heappop(rh)
        heapq.heappush(lh, q)
        heapq.heappush(rh, p)
    print(-1*lh[0])