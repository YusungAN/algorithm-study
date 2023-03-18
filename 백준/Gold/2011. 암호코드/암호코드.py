import sys

input = sys.stdin.readline
n = list(map(int, list(input().rstrip())))
dp = [0]*(len(n)+1)
dp[0] = 1
dp[1] = 1
if n[0] == 0:
    print(0)
    exit(0)
for i in range(2, len(n)+1):
    if n[i-1] == 0:
        if 0 < n[i-2] <= 2:
            dp[i] = dp[i-2]
        else:
            print(0)
            exit(0)
    elif n[i-2] != 0 and n[i-2]*10+n[i-1] <= 26:
        dp[i] = (dp[i-2]+dp[i-1])%1000000
    else:
        dp[i] = dp[i-1]
print(dp[-1])
