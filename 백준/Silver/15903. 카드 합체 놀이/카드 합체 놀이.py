import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
q = []
for i in li:
    heappush(q, i)

for _ in range(m):
    a = heappop(q)
    b = heappop(q)
    heappush(q, a+b)
    heappush(q, a+b)

print(sum(q))