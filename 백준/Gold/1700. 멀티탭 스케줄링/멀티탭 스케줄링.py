import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
last = [deque() for _ in range(k+1)]
for idx, item in enumerate(li):
    last[item].append(idx)
now = [0]*n

ans = 0
for i in range(k):
    if li[i] in now:
        if len(last[li[i]]) > 0:
            last[li[i]].popleft()
        # print(now)
        # print(last)
        # print('-----------------')
        continue
    if 0 in now:
        now[now.index(0)] = li[i]
        last[li[i]].popleft()
        # print(now)
        # print(last)
        # print('------------------')
        continue

    outed = 0
    outed_idx = 0
    for j in now:
        if len(last[j]) == 0:
            outed_idx = j
            break
        now_val = last[j].popleft()
        if outed < now_val:
            outed = now_val
            outed_idx = j
        last[j].appendleft(now_val)

    now[now.index(outed_idx)] = li[i]
    if len(last[li[i]]) > 0:
        last[li[i]].popleft()
    ans += 1
    # print(now)
    # print(last)
    # print('-------------------------')

print(ans)
