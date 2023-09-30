import sys

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
li = [tuple(map(int, input().split())) for _ in range(M)]

li.sort(key=lambda x: x[1])

store = [0]*(N+1)
ans = 0
for i in range(M):
    s, e, w = li[i]
    now_max = 0
    for j in range(s, e):
        now_max = max(now_max, store[j])
    if now_max < C:
        # print('asdf', s, e, w)
        # store[e] -= w if store[s]+w <= C else C - store[s]
        now = w if now_max + w <= C else C - now_max
        ans += now
        for j in range(s, e):
            store[j] += now

    # print(store, ans)

print(ans)
