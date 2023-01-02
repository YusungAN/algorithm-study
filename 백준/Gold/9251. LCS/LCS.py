import sys
# import time

# start = time.time()

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

lena = len(a)
lenb = len(b)
dp = [[0]*lena for i in range(lenb+1)]
for i in range(lenb):
    max_tmp = 0
    for j in range(lena):
        if a[j] == b[i]:
            if j > 0:
                dp[i+1][j] = max_tmp+1
            else:
                dp[i+1][j] += 1
        else:
            dp[i+1][j] = dp[i][j]
        if dp[i][j] > max_tmp:
            max_tmp = dp[i][j]

    # print(dp)

print(max(dp[-1]))
# print(time.time()-start)