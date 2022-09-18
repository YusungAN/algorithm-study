import sys

input = sys.stdin.readline

pdm_n = int(input())
pdm_w = list(map(int, input().split(' ')))
marb_n = int(input())
marb_w = list(map(int, input().split(' ')))

res = []
marb_max = max(marb_w)
#print(marb_max)
dp = [[0]*(30*500) for _ in range(pdm_n)]

for i in range(pdm_n):
    if i == 0:
        for j in range(30*500):
            if j == pdm_w[i]-1:
                dp[i][j] = 1
        #print(dp)
        continue
    w = pdm_w[i]
    for j in range(30*500):
        # print(j, j+w-1, abs(j-w)-1)
        if dp[i-1][j] == 1 or j == w-1 or (j+w < 30*500 and dp[i-1][j+w]) == 1 or dp[i-1][abs(j+1-w)-1] == 1:
            dp[i][j] = 1
    #print(dp)

for i in marb_w:
    if i > 30*500:
        print('N', end=' ')
        continue
    print('Y' if dp[-1][i-1] == 1 else 'N', end=' ')