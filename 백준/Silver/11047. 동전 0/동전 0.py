N, K = map(int, input().split())
coin = []
cnt = 0

for i in range(N):
    coin.append(int(input()))

for i in range(N):
    if coin[N-i-1] <= K:
        cnt += K // coin[N-i-1]
        K -= (K // coin[N-i-1]) * coin[N-i-1]

print(cnt)