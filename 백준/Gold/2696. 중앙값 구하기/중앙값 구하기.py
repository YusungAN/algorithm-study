import sys
from heapq import heappush, heappop

input = sys.stdin.readline

for _ in range(int(input())):
    lh = []
    rh = []
    res = []
    n = int(input())
    li = []
    for i in range(n//10+1):
        li.extend(list(map(int, input().split(' '))))
    print(len(li)//2+1)
    for i in range(len(li)):
        if len(lh) == len(rh):
            heappush(lh, -1*li[i])
        else:
            heappush(rh, li[i])
        if len(rh) > 0 and -1*lh[0] > rh[0]:
            p = -1*heappop(lh)
            q = -1*heappop(rh)
            heappush(lh, q)
            heappush(rh, p)
        if i % 2 == 0:
            res.append(-1*lh[0])

    print(*res)
