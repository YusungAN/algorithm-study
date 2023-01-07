import sys

input = sys.stdin.readline

s = input().rstrip()
slen = len(s)
dp = [[0]*(slen+1) for _ in range(slen+1)]

for size in range(1, slen+1):
    for start in range(1, slen+1):
        end = start+size-1
        if end > slen:
            continue
        if size == 1:
            dp[start][end] = 1
        elif size == 2:
            if s[start-1] == s[end-1]:
                dp[start][end] = 1
        else:
            if dp[start+1][end-1] == 1 and s[start-1] == s[end-1]:
                dp[start][end] = 1

dp2 = [2500 for _ in range(slen+1)]
dp2[0] = 0
for end in range(1, slen+1):
    dp2[end] = dp2[end-1]+1
    for start in range(1, end):
        if dp[start][end]:
            dp2[end] = min(dp2[end], dp2[start-1]+1)

print(dp2[slen])
