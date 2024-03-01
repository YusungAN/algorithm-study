import sys

input = sys.stdin.readline

N, L = map(int, input().split())
li = [tuple(map(int, input().split())) for _ in range(N)]

li.sort(key=lambda x: x[0])

ans = 0
now = 0
for s, e in li:
    if now < s:
        now = s
    while now < e:
        now += L
        ans += 1

print(ans)