import sys

input = sys.stdin.readline

n = int(input())
p_list = [0]+list(map(int, input().split()))

dp = [0]*(n+1)

dp[1] = p_list[1]

for i in range(2, n+1):
    max_tmp = 0
    for j in range(1, i+1):
        max_tmp = max(dp[i-j]+p_list[j], max_tmp)

    dp[i] = max_tmp

# print(dp)
print(dp[n])