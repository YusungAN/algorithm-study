import sys

input = sys.stdin.readline

n, t = map(int, input().split(' '))
remained = 0
prev_day = -1
ans = 0
for _ in range(n):
    d, b = map(int, input().split(' '))
    if prev_day != -1:
        ans += min(remained, d-1-prev_day)
        remained -= min(remained, d-1-prev_day)
    remained += b
    ans += 1
    remained -= 1
    prev_day = d

if prev_day < t:
    ans += min(remained, t-prev_day)
print(ans)
